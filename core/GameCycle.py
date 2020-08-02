import pygame

class GameCycle:

	def start():
		pygame.init()		

		clock = pygame.time.Clock()

		while not GameCycle.gameEnd():
			clock.tick(60)

		pygame.quit()
		quit()

	def gameEnd():
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return True
			if pygame.key.get_pressed()[pygame.K_ESCAPE]:
				return True


