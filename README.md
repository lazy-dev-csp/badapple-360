# badapple-360

Plays ASCII art animations on Xbox 360 (or any low-memory system). Optimized for 512MB RAM PowerPC systems whit python 2.6.6(may not work on newer systems)

## Requirements

- Python 2.6.6+
- FFmpeg
- A video file (works great with high-contrast videos like Bad Apple)

## Setup

### 1. Convert Video to 24fps

```bash
ffmpeg -i video.mp4 -filter:v fps=24 video_24fps.mp4
```

## 2. Extract Frames
```bash mkdir frames
ffmpeg -i video_24fps.mp4 -vf "scale=60:-1" frames/frame_%06d.png
```

# 3. Convert Frames to ASCII
```bahs python converter.py
This reads from frames/ and creates ascii_frames.zip
```

# 4. Play the Animation
```bash python player.py
```
**Configuration**(optional if you followed the previous steps)

Edit player.py to adjust:
fps = 24 - Match your video's fps
zip_path = "ascii_frames.zip" - Path to your ASCII frames
Edit image_to_ascii.py to adjust:
new_width = 60 - Must match the scale= value from step 2
threshold = 128 - ASCII conversion threshold (good for high-contrast videos)
Performance Tips
If playback freezes or stutters:
Reduce frame width: scale=50:-1 or scale=40:-1
Lower fps: fps=20
Use less compression: zip -0 -r ascii_frames.zip ascii_frames/
**Memory usage guide:**
60 width @ 24fps: ~7-5MB
50 width @ 24fps: ~5-4MB
40 width @ 20fps: ~4-3MB

**How It Works:**

Video is converted to static PNG frames
Frames are converted to ASCII text files
ASCII files are compressed into a zip
Player reads and displays frames from zip in real-time
