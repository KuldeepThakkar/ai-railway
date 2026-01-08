from fastapi import FastAPI, WebSocket, WebSocketDisconnect, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.streamer import VideoStreamer
from app.utils import extract_frames_from_video
import asyncio
import os
import shutil

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize Streamer
# path to dataset
DATASET_PATH = r"c:\New folder\blurred_sharp"
MODEL_PATH = "checkpoints/best_model.pth"
DEVICE = "cpu" # Default to CPU for safer demo on mixed hardware

streamer = VideoStreamer(DATASET_PATH, MODEL_PATH, DEVICE)

@app.on_event("startup")
async def startup_event():
    # Start streamer in background
    asyncio.create_task(streamer.start_stream())

@app.get("/")
def read_root():
    return {"status": "Railway Inspection AI Online"}

@app.get("/stats")
def get_stats():
    return streamer.stats

@app.post("/upload_video")
async def upload_video(file: UploadFile = File(...)):
    try:
        # Define paths
        temp_video_path = f"temp_{file.filename}"
        # Store extracted frames in a 'custom_upload' folder inside the dataset path or a separate temp folder
        # For simplicity, creating a new folder beside the app
        output_dir = os.path.join(os.getcwd(), "uploaded_frames")
        
        # Save uploaded video
        with open(temp_video_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
            
        # Clear existing frames in output directory if any
        if os.path.exists(output_dir):
            shutil.rmtree(output_dir)
        os.makedirs(output_dir)
        
        # Extract frames
        num_frames = extract_frames_from_video(temp_video_path, output_dir)
        
        # Cleanup video file
        os.remove(temp_video_path)
        
        # Update Streamer
        success = streamer.reload_images(output_dir)
        
        if not success:
             raise HTTPException(status_code=500, detail="Failed to load images from extracted video")

        return {
            "message": "Video processed successfully",
            "frames_extracted": num_frames,
            "status": "Stream updated"
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            if streamer.latest_frame_data:
                await websocket.send_json(streamer.latest_frame_data)
            await asyncio.sleep(0.05) # Send at approx 20fps
    except WebSocketDisconnect:
        print("Client disconnected")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
