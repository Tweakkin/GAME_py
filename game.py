import pygame

pygame.init()
WIN_WIDTH = 720
WIN_HEIGHT = 950
screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
background = pygame.image.load("background.jpeg")
PLAYER_WIDTH = 150
PLAYER_HEIGHT = 150
player = pygame.image.load("thorfinn_player.png").convert_alpha()
player = pygame.transform.scale(player, (PLAYER_WIDTH, PLAYER_HEIGHT))
clock = pygame.time.Clock()

def draw():
	screen.blit(background, (0, 0))
	screen.blit(player, (100, 100))

def main():
	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
		draw()
		pygame.display.flip()
		clock.tick(60)
	pygame.quit()

if __name__ == "__main__":
	main()