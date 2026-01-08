import asyncio
import cv2
import torch
import numpy as np
from PIL import Image
from ml.model import DeblurUNet
import os
import time
import base64
from io import BytesIO

class VideoStreamer:
    def __init__(self, dataset_path, model_path=None, device="cpu"):
        self.device = device
        self.model = DeblurUNet().to(device)
        self.dataset_path = dataset_path
        self.blur_path = os.path.join(dataset_path, "blurred_sharp", "blurred")

        # Load model if exists, else utilize random init (demo mode)
        if model_path and os.path.exists(model_path):
            self.model.load_state_dict(torch.load(model_path, map_location=device))
            print("Model loaded successfully.")
        else:
            print("Warning: No model found. Using random weights.")
        
        self.model.eval()
        
        self.image_files = [
            os.path.join(self.blur_path, f) 
            for f in sorted(os.listdir(self.blur_path)) 
            if f.endswith(('.png', '.jpg'))
        ]
        self.current_idx = 0
        self.running = False
        self.latest_frame_data = None
        self.stats = {"fps": 0, "processed_count": 0, "avg_inference_time": 0}
    
    def reload_images(self, new_dir):
        """Reloads images from a new directory."""
        if not os.path.exists(new_dir):
            print(f"Directory not found: {new_dir}")
            return False
            
        new_files = [
            os.path.join(new_dir, f) 
            for f in sorted(os.listdir(new_dir)) 
            if f.endswith(('.png', '.jpg', '.jpeg'))
        ]
        
        if not new_files:
            print(f"No images found in {new_dir}")
            return False
            
        self.running = False  # Pause stream briefly
        self.image_files = new_files
        self.current_idx = 0
        self.running = True   # Resume
        print(f"Reloaded streamer with {len(new_files)} images from {new_dir}")
        return True

    async def start_stream(self):
        self.running = True
        print("Stream started...")
        while self.running:
            start_time = time.time()
            
            # 1. Get Image
            if not self.image_files:
                await asyncio.sleep(1)
                continue
                
            img_path = self.image_files[self.current_idx]
            original_img = Image.open(img_path).convert("RGB")
            
            # 2. Preprocess
            img_tensor = torch.from_numpy(np.array(original_img)).permute(2, 0, 1).float() / 255.0
            img_tensor = img_tensor.unsqueeze(0).to(self.device)
            
            # 3. Inference
            inf_start = time.time()
            with torch.no_grad():
                enhanced_tensor = self.model(img_tensor)
            inf_time = time.time() - inf_start
            
            # 4. Postprocess
            enhanced_img = enhanced_tensor.squeeze(0).permute(1, 2, 0).cpu().numpy()
            enhanced_img = (enhanced_img * 255).astype(np.uint8)
            original_numpy = np.array(original_img)

            # 5. Encode images to base64 for frontend
            def to_b64(img_arr):
                img_pil = Image.fromarray(img_arr)
                buff = BytesIO()
                img_pil.save(buff, format="JPEG")
                return base64.b64encode(buff.getvalue()).decode("utf-8")

            self.latest_frame_data = {
                "original": to_b64(original_numpy),
                "enhanced": to_b64(enhanced_img),
                "filename": os.path.basename(img_path),
                "inference_time": f"{inf_time*1000:.2f}ms"
            }
            
            # Update Stats
            self.current_idx = (self.current_idx + 1) % len(self.image_files)
            self.stats["processed_count"] += 1
            self.stats["avg_inference_time"] = (self.stats["avg_inference_time"] * 0.9) + (inf_time * 0.1)
            
            loop_duration = time.time() - start_time
            self.stats["fps"] = 1.0 / max(loop_duration, 0.001)
            
            await asyncio.sleep(0.03) # Simulate ~30 FPS cap if inference is too fast

    def stop_stream(self):
        self.running = False
