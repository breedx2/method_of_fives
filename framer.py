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

meta = VideoMeta(FFPROBE_BIN).read(sys.argv[1])
print("Video file metadata: ")
for k,v in meta.items():
	print("%s: %s" % (k,v))
print("----------------------------")

filename = sys.argv[1]

framegen = FrameGenerator.build(FFPROBE_BIN, FFMPEG_BIN, filename, 1)

# command = [ FFMPEG_BIN,
#             '-i', filename,
#             '-f', 'image2pipe',
#             '-pix_fmt', 'gray',
#             '-vcodec', 'rawvideo', '-']
# pipe = sp.Popen(command, stdout = sp.PIPE, bufsize=10**8)

for i in range(0,10):

	# read 1 frame (assumes 3 bytes per pixel)
	# raw_image = pipe.stdout.read(meta['width'] * meta['height'] * 3)
	# raw_image = pipe.stdout.read(meta['width'] * meta['height'] * 1) # 1 byte per pixel with pix_fmt gray

	# Test that the frame looks right by saving it to a raw .data file
	# f = open('/tmp/outfile.data', 'w')
	# for i in range(0, meta['width'] * meta['height']):
	# 	f.write(raw_image[i])
	# 	f.write(raw_image[i])
	# 	f.write(raw_image[i])
	# f.close()



	# image =  numpy.fromstring(raw_image, dtype='uint8')
	# image = image.reshape((meta['height'], meta['width']))
	# pipe.stdout.flush()

	image = framegen.next()

	f = open('/tmp/outfile%d.data' % (i), 'w')
	for y in range(0, image.shape[0]):	# height
		for x in range(0, image.shape[1]):
			f.write(chr(image[y, x]))
			f.write(chr(image[y, x]))
			f.write(chr(image[y, x]))
	f.close()


	# print(">>>>>>>>>>>>>>>>>>> %d %d %d" % (image[212,210,0], image[212,210,1], image[210,212,2]))

