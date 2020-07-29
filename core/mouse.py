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

	def calcalculateMouseStep(self):
		self.mouse.generateMouse()
		self.mouse.stepMouse()

	def generateMouse(self):
		self.mouse.append(Mouse((random.randrange(10, self.display.width - 10), 
						   		 random.randrange(10, self.display.height - 10))))

	def stepMouse(self):
		self.mouse.append(Mouse((random.randrange(10, self.display.width - 10), 
						   		 random.randrange(10, self.display.height - 10))))

	def  paint(self, display):
		self.mouse = mouse