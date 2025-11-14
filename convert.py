# -*- coding: utf-8 -*-
from __future__ import print_function
import os
from PIL import Image
import zipfile

frames_dir = "frames"
output_dir = "ascii_frames"
new_width = 40
threshold = 100

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

frame_files = sorted([f for f in os.listdir(frames_dir) if f.endswith(".png")])

for i, filename in enumerate(frame_files):
    img_path = os.path.join(frames_dir, filename)
    img = Image.open(img_path).convert("L")
    
    width, height = img.size
    aspect_ratio = height / float(width)
    new_height = int(aspect_ratio * new_width * 0.55)
    
    img = img.resize((new_width, new_height))
    
    pixels = img.load()
    ascii_frame = []
    
    for y in range(new_height):
        line = []
        for x in range(new_width):
            pixel = pixels[x, y]
            if pixel < threshold:
                line.append("\033[40m \033[0m")
            else:
                line.append("\033[47m \033[0m")
        ascii_frame.append("".join(line))
    
    output_filename = "frame_%06d.txt" % (i + 1)
    output_path = os.path.join(output_dir, output_filename)
    
    with open(output_path, "w") as f:
        f.write("\n".join(ascii_frame))
    
    if (i + 1) % 100 == 0:
        print("[#] Processed %d/%d frames" % (i + 1, len(frame_files)))

print("\n[#] Creating zip archive...")
with zipfile.ZipFile("ascii_frames.zip", "w", zipfile.ZIP_DEFLATED) as zf:
    for filename in sorted(os.listdir(output_dir)):
        if filename.endswith(".txt"):
            file_path = os.path.join(output_dir, filename)
            zf.write(file_path, filename)

print("[+] Created ascii_frames.zip")
