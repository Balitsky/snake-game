import pygame
from ui.MainScene import MainScene

class GameCycle:

	def start():
		pygame.init()		

		clock = pygame.time.Clock()

		pygame.init()
		display = pygame.display.set_mode((500, 500))

		currentScene = MainScene(display)

		while not GameCycle.gameEnd():
			currentScene.render()
			clock.tick(60)

		pygame.quit()
		quit()

	def gameEnd():
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return True
			if pygame.key.get_pressed()[pygame.K_ESCAPE]:
				return True


