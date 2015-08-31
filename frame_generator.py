import subprocess as sp
import numpy
from metadata import VideoMeta

class FrameGenerator(object):

	@staticmethod
	def build(ffprobe, ffmpeg, filename, bpp):
		meta = VideoMeta(ffprobe).read(filename)
		return FrameGenerator(ffmpeg, bpp, filename, meta)

	def __init__(self, ffmpeg, bpp, filename, meta):
		self.ffmpeg = ffmpeg
		self.bpp = bpp # bytes per pixel
		self.filename = filename
		self.meta = meta
		self.pipe = None

	def __iter__(self):
		return self

	def __next__(self):
		return self.next()

	def next(self):
		self._lazy_init()
		raw_image = self.pipe.stdout.read(self.meta['width'] * self.meta['height'] * self.bpp)
		image =  numpy.fromstring(raw_image, dtype='uint8')
		if self.bpp == 1:
			image = image.reshape(self.meta['height'], self.meta['width'])
		if self.bpp == 1:
			image = image.reshape(self.meta['height'], self.meta['width'], self.bpp)
		self.pipe.stdout.flush()
		# TODO: Determine safe finishing/done state
		if(False):
			raise StopIteration()
		return image

	def _lazy_init(self):
		if not self.pipe:
			command = [ self.ffmpeg,
	            '-i', self.filename,
	            '-f', 'image2pipe',
	            '-pix_fmt', self._ffmpeg_format(),
	            '-vcodec', 'rawvideo', '-']
			self.pipe = sp.Popen(command, stdout = sp.PIPE, bufsize=10**8)

	def _ffmpeg_format(self):
		if(self.bpp == 1):
			return 'gray'
		if(eslf.bpp == 3):
			return 'rgb24'
		raise Exception('Unhandled byte depth: %d' %(self.bpp))

	def _framebuf_size(self):
		return self.meta['width'] * self.meta['width'] * self.bpp