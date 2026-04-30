import pygame


WIDTH, HEIGHT = 1280, 720
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.init()


def main():
	run = True
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			WIN.fill((255, 255, 255))

			pygame.display.flip()
			pygame.display.set_caption("Game")
	pygame.quit()



if __name__ == "__main__":
	main()