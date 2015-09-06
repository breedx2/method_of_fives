
def average(rect):
	total = reduce( lambda x,y: x+y, map(sum, rect))
	v = total * 1.0 / (rect.shape[0] * rect.shape[1])
	return int((v * 65535)/255)