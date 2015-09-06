import sys
import subprocess as sp
import numpy
from metadata import VideoMeta
from frame_generator import FrameGenerator
from image_analyze import slice_averages

FFMPEG_BIN = 'ffmpeg'
FFPROBE_BIN = 'ffprobe'

def usage():
	print("Usage: %s <filename>" % (sys.argv[0]))
	sys.exit(1)

if len(sys.argv) < 2:
	usage()

filename = sys.argv[1]

framegen = FrameGenerator.build(FFPROBE_BIN, FFMPEG_BIN, filename, 1)

print("Video file metadata: ")
for k,v in framegen.meta.items():
	print("%s: %s" % (k,v))
print("----------------------------")

width = framegen.meta['width']
height = framegen.meta['height']
dx = width / 5
dy = height / 5
slices = []
for image in framegen:
	averages = slice_averages(image)
	print(averages)
