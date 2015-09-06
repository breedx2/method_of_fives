
import numpy

def average(rect):
	total = reduce( lambda x,y: x+y, map(sum, rect))
	v = total * 1.0 / (rect.shape[0] * rect.shape[1])
	return int((v * 65535)/255)

def to_16(sum, width, height):
	avg = sum * 1.0 / (width * height)
	return int( (avg * 65535) / 255)

# Return a 5x5 array containing averages for slices
def compute_averages(image, dx, dy):
	sums = compute_sums(image, dx, dy)
	y_sums = [reduce(lambda a,b: a+b, sums[y]) for y in range(0,5)]
	y_avg = map(lambda t: to_16(t, image.shape[1], dy), y_sums)
	x_sums = [reduce(lambda a,b: a+b, sums[0:5,x]) for x in range(0,5)]
	x_avg = map(lambda t: to_16(t, dx, image.shape[0]), x_sums)
	return [x_avg, y_avg]

# Return a 5x5 array containing sums for rects
def compute_sums(image, dx, dy):
	# First reduce to a 5x5 of sums
	sums = []
	for y in range(0,5):
		def summer(x):
			rect = image[y*dy:(y+1)*dy,x*dx:(x+1)*dx]
			return reduce( lambda a,b: a+b, map(sum, rect))
		sums.append( [summer(x) for x in range(0,5)])
	return numpy.array(sums)