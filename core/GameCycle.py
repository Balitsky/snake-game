import pygame
from core.Window import Window
from core.Controller import Controller

class GameCycle:

	def start():
		pygame.init()		
		window = Window(title = "Main Display")

		controller = Controller(window)

		clock = pygame.time.Clock()

		while not GameCycle.gameEnd():

			
			controller.prepareNextStep()
			window.update()

			clock.tick(60)

		pygame.quit()

	def gameEnd():
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return True
			if pygame.key.get_pressed()[pygame.K_ESCAPE]:
				return True


