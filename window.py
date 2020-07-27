import pygame

class Window:
	global display
	global width
	global height

	def __init__(self, width = 640, height = 480, title = "new window"):
		display = pygame.display.set_mode((width, height))
		pygame.display.set_caption(title)
		pygame.display.update()
			
		self.display = display
		self.width = width
		self.height = height


	def paint(self, pos, size, color = (0, 255, 0)):
		return pygame.draw.rect(self.display, color, [pos[0], pos[1], size[0], size[1]])
	
	def invalidatePos(self, pos):
		if pos[0] > self.width:
			return (0, pos[1])
		elif pos[0] < 0:
			return (self.width, pos[1])
		elif pos[1] < 0:
			return (pos[0], self.height)
		elif pos[1] > self.height:
			return (pos[0], 0)
		return pos	


	def clear(self):
		self.display.fill((0,0,0))

	def update(self):
		pygame.display.update()
