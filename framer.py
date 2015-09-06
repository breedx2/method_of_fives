import sys
import subprocess as sp
import numpy
from metadata import VideoMeta
from frame_generator import FrameGenerator
from image_analyze import average

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
	def slice_dx(x):
		start = x*dx
		end = (x+1)*dx
		rect = image[0:height,start:end]
		return average(rect)
	def slice_dy(y):
		start = y*dy
		end = (y+1)*dy
		rect = image[start:end,0:width]
		return average(rect)
	x_slices = [slice_dx(x) for x in range(0,5) ]
	y_slices = [slice_dy(y) for y in range(0,5) ]
	print("x_slices :: %s" %(x_slices))
	print("y_slices :: %s" %(y_slices))
	slices.append([x_slices,y_slices])