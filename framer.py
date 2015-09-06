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

dx = framegen.meta['width'] / 5
dy = framegen.meta['height'] / 5
frames = []
for image in framegen:
	averages = slice_averages(image)
	# print(averages)
	frames.append(averages)

print("Data collected for %d frames!" %(len(frames)))

def write_files(frames, file_prefix, index):
	for i in range(0,5):
		filename = '%s%d.raw' %(file_prefix, i)
		print("Writing data to %s" %(filename))
		f = open(filename, 'wb')
		for pair in frames:
			f.write(pair[index][i])
		f.close()
		print("Done writing %s" %(filename))

write_files(frames, 'x', 0)
write_files(frames, 'y', 1)