# -*- coding: utf-8 -*-
from __future__ import print_function
import zipfile
import time
import sys
import gc

zip_path = "ascii_frames.zip"
fps = 24
frame_delay = 1.0 / fps

for i in range(5, 0, -1):
    sys.stdout.write("%d...\r" % i)
    sys.stdout.flush()
    time.sleep(1)

sys.stdout.write("\033[?25l\033[2J\033[H")
sys.stdout.flush()

write = sys.stdout.write
flush = sys.stdout.flush
time_func = time.time
cursor_home = "\033[H"

zf = zipfile.ZipFile(zip_path, "r")
frame_names = sorted([n for n in zf.namelist() if n.endswith(".txt")])

start_time = time_func()
next_frame_time = start_time

try:
    for idx, name in enumerate(frame_names):
        write(cursor_home)
        write(zf.read(name))
        flush()
        
        if idx % 500 == 0:
            gc.collect()
        
        next_frame_time += frame_delay
        sleep_time = next_frame_time - time_func()
        
        if sleep_time > 0:
            time.sleep(sleep_time)
finally:
    zf.close()
    sys.stdout.write("\033[?25h")
    sys.stdout.flush()

print("\nPlayback finished!")
