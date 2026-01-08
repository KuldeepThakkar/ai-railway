import cv2
import os

def extract_frames_from_video(video_path, output_dir, verbose=False):
    """
    Extracts all frames from a video file and saves them as images in the output directory.
    If verbose is True, prints progress to console.
    Returns the number of frames saved.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)
        if verbose:
            print(f"Created output directory: {output_dir}")

    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        raise ValueError(f"Could not open video file {video_path}")

    # Get video properties
    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    if verbose:
        print(f"Processing {video_path}")
        print(f"FPS: {fps}, Total Frames (approx): {total_frames}")

    frame_count = 0
    saved_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break
            
        frame_filename = os.path.join(output_dir, f"frame_{frame_count:06d}.jpg")
        cv2.imwrite(frame_filename, frame)
        saved_count += 1
        frame_count += 1
        
        if verbose and frame_count % 100 == 0:
            print(f"Extracted {frame_count} frames...")

    cap.release()
    return saved_count
