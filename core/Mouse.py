import random

class Mouse:

	global dimensions
	global speed
	global size
	global pos
	direction = (0, 0)


	def __init__(self, display, dimensions = (15, 15) ):
		self.dimensions = dimensions
		self.pos = (random.randrange(10, display.width - 10),
		            random.randrange(10, display.height - 10))
		self.speed = 1

	def calcalculateMouseStep(self):
		self.getDirection()
		newPos = (self.pos[0] + self.speed * self.direction[0],
				  self.pos[1] + self.speed * self.direction[1])
		self.pos = newPos

	def paint(self, display):
		self.validatePos(display)
		display.paint(self.pos, self.dimensions, color = (9, 27, 242))

	def getDirection(self):
		if random.randrange(0, 1000) > 950:
			self.direction = (round(random.randrange(-1, 2)),
					          round(random.randrange(-1, 2)))
	def validatePos(self, display):
		self.pos = display.invalidatePos(self.pos)
		



