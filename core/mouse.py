class Mouse:

	global dimensions
	global speed
	global size
	global pos

	def __init__(self, pos, dimensions = (10, 10) ):
		self.dimensions = dimensions
		self.size = 1
		self.pos = pos
		self.speed = 1
