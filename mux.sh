#!/bin/bash

# Script to mux audio and video together

AUDIO=$1
VIDEO=/home/jason/media/VID_20150626_191903.mp4

ffmpeg -i ${VIDEO} -i ${AUDIO} -strict -2 -c copy -acodec mp3 -q:a 0 out.mp4