import pygame

def execute(callback):
	print("Hello")
	callback()

def game():
	pygame.init()

	mainSurface = pygame.display.set_mode((1000, 1000))
	imageSurface = pygame.transform.scale(pygame.image.load("image.png"), (1000, 1000))

	mainSurface.blit(imageSurface, (0, 0))


	textSurface: pygame.Sufrase = pygame.font.Font(pygame.font.get_default_font(), 32).render("Качоооок", True, pygame.Color("#18FF00"))

	smallKek = pygame.transform.scale(imageSurface, (100, 100))
	smallKek.set_clip((0, 0, 50, 50))
	smallKek.blit(textSurface, (0, 0))



	smallRect = mainSurface.blit(smallKek, (200, 200))



	pygame.display.update()
	pygame.time.wait(2000)


	
	mainSurface.blit(mainSurface, smallRect, smallRect)

	pygame.display.update()
	pygame.time.wait(2000)







execute(game)