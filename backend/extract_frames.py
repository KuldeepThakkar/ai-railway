import argparse
import os
import sys

# Ensure we can import from app
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.utils import extract_frames_from_video

def main():
    parser = argparse.ArgumentParser(description="Extract all frames from a video file (e.g., .ts, .mp4).")
    parser.add_argument("video_path", help="Path to the input video file")
    parser.add_argument("output_dir", help="Directory to save extracted frames")
    
    args = parser.parse_args()
    
    print(f"Processing {args.video_path}...")
    try:
        count = extract_frames_from_video(args.video_path, args.output_dir, verbose=True)
        print(f"Done! Extracted {count} frames to {args.output_dir}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
