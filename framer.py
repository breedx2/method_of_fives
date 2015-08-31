import sys
import subprocess as sp
#import numpy
from metadata import VideoMeta

FFMPEG_BIN = 'ffmpeg'
FFPROBE_BIN = 'ffprobe'

def usage():
	print("Usage: %s <filename> <width> <height>" % (sys.argv[0]))
	sys.exit(1)

if len(sys.argv) < 2:
	usage()

meta = VideoMeta(FFPROBE_BIN).read(sys.argv[1])
print "GOT RESULT: " 
for k,v in meta.items():
	print("%s: %s" % (k,v))
sys.exit(0)	# debuggery

# filename = sys.argv[1]
# width = sys.argv[2]
# height = sys.argv[3]

# command = [ FFMPEG_BIN,
#             '-i', filename,
#             '-f', 'image2pipe',
#             '-pix_fmt', 'rgb24',
#             '-vcodec', 'rawvideo', '-']
# pipe = sp.Popen(command, stdout = sp.PIPE, bufsize=10**8)

# # read 420*360*3 bytes (= 1 frame)
# raw_image = pipe.stdout.read(420*360*3)

# print("%d %d %d" % (raw_image[0],  raw_image[1], raw_image[2]));

