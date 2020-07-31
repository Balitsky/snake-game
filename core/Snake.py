class Snake:

	global dimensions
	global size
	global speed
	global position

	def __init__(self, startPosition, dimensions = (10, 10)):
		self.dimensions = dimensions
		self.size = 1
		self.speed = 1.5
		self.position = [startPosition]

	def calculatePosition(self, direction):
		newPos = (self.headPosition()[0] + direction[0]*self.speed, 
				  self.headPosition()[1] + direction[1]*self.speed)
		self.position.insert(0, newPos)	
		self.deleteLast()

		return self.position

	def addChunk(self, direction):
		for i in [1,2,3,4,5,6,7,8,9]:
			newPos = (self.headPosition()[0] + direction[0]*self.speed, 
					  self.headPosition()[1] + direction[1]*self.speed)
			self.position.insert(0, newPos)			
		
	def headPosition(self):
		return self.position[0]

	def deleteLast(self):
		del self.position[-1]

	def updateHeadPos(self, pos):
		self.position[0] = pos
		
