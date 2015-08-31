import sys
import subprocess as sp
import numpy
from metadata import VideoMeta
from frame_generator import FrameGenerator

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

i = 0
for image in framegen:
	f = open('/tmp/outfile%d.data' % (i), 'w')
	for y in range(0, image.shape[0]):	# height
		for x in range(0, image.shape[1]):
			f.write(chr(image[y, x]))
			f.write(chr(image[y, x]))
			f.write(chr(image[y, x]))
	f.close()
	i = i + 1
