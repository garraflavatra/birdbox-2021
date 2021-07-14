#!/usr/bin/python3

import sys
import os
import time

def stream_youtube():
    """
    Stream to YouTube.

    This function reads the YT streaming key from youtube-key.txt and executes
    Raspivid and FFmpeg.
    """
    while True:
        # Read stream key
        with open('/opt/birdbox/youtube-key.txt') as f:
            yt_key = f.readline()

        # Concatenate command and key
        command = 'raspivid -o - -t 0 -w 1280 -h 720 -fps 25 -b 4000000 -g 50 | ffmpeg -re -ar 44100 -ac 2 -acodec pcm_s16le -f s16le -ac 2 -i /dev/zero -f h264 -i - -vcodec copy -acodec aac -ab 128k -g 50 -strict experimental -f flv rtmp://a.rtmp.youtube.com/live2/%s' %(yt_key)

        # Execute command
        os.system(command)

        # Wait before doing it again to kill connection
        time.sleep(5)

if __name__ == '__main__':
    """
    Execute the function if this file is not imported by another.
    """
    stream_youtube()
