
import numpy

def slice_averages(image):
	dx = image.shape[1]/5
	dy = image.shape[0]/5
	def scale(a):
		return int( ((a * 65535) / 255) - (65535.0/2))
	x_avg = [ image[0:image.shape[0],x*dx:(x+1)*dx].mean() for x in range(0,5)]
	x_avg = numpy.array(map(scale, x_avg), dtype='int16')
	y_avg = [ image[y*dy:(y+1)*dy,0:image.shape[1]].mean() for y in range(0,5)]
	y_avg = numpy.array(map(scale, y_avg), dtype='int16')
	return [x_avg, y_avg]
