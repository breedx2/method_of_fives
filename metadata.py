# read some metadata for a video file using an ffprobe subprocess
import subprocess as sp
import os

class VideoMeta(object):
	def __init__(self, ffprobe):
		self.ffprobe = ffprobe

	def read(self, filename):
		meta = self._read_meta(filename)
		return self._parse_meta(meta)

	def _read_meta(self, filename):
		return self._read_output([
				self.ffprobe,
				'-v', 'error',
				'-select_streams', 'v:0',
				'-show_entries', 'stream=duration',
				'-show_entries', 'stream=height,width',
				'-show_entries', 'stream=avg_frame_rate',
				'-of', 'default=noprint_wrappers=1',
				filename
			])

	def _parse_meta(self, meta):
		meta = self._to_dict(meta)
		meta['fps'] = self._munge_rate(meta['avg_frame_rate'])
		return meta

	def _to_dict(self, meta):
		result = dict()
		for line in meta:
			k,v = line.split(r'=')
			result[k] = v
		return result

	def _munge_rate(self, rate):
		num,den = rate.split(r'/')
		return float(num)/float(den)

	def _read_output(self, command):
		pipe = sp.Popen(command, stdout = sp.PIPE, bufsize=10**8)
		output, error = pipe.communicate()
		return output.splitlines()