import pygame
import random
import game_utils

pygame.init()
WIN_WIDTH = 720
WIN_HEIGHT = 950
screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
lost_sound = pygame.mixer.Sound("./sounds/game_over.mp3")
background = pygame.image.load("./imgs/background.jpeg")
pygame.mixer.music.load("./sounds/game_sound.mp3")
pygame.mixer.music.play(-1) 
PLAYER_WIDTH = 150
PLAYER_HEIGHT = 150
player = pygame.Rect(100, WIN_HEIGHT-(PLAYER_HEIGHT * 2), PLAYER_WIDTH, PLAYER_HEIGHT - 75)
obj_rect = pygame.Rect(random.randint(0, 720), 0, 30,30)
speed = 5
player_image = pygame.image.load("./imgs/bird.png").convert_alpha()
rock_image = pygame.image.load("./imgs/rock_2.png").convert_alpha()
intro_image = pygame.image.load("./imgs/intro.png").convert_alpha()
clock = pygame.time.Clock()

def draw(seconds, obj_rect):
	font = pygame.font.Font(None, 70)
	timer_text = font.render(f"{seconds}", 1 , "red")
	screen.blit(background, (0, 0))
	screen.blit(player_image, player)
	screen.blit(timer_text, (360, 150))
	for obj in obj_rect:
		screen.blit(rock_image, obj)
	
def main():
	game_utils.introduction(screen, background, intro_image, clock)
	timer = 0
	running = True
	obj_rect = [pygame.Rect(random.randint(0, 720), 0, 30,30) for _ in range(3)]
	while running:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
		for i in range(len(obj_rect)):
			obj = obj_rect[i]
			if obj.bottom > WIN_HEIGHT:
				obj_rect[i] = pygame.Rect(random.randint(0, 720), 0,30, 30)
			if player.colliderect(obj):
				game_utils.handle_loss(seconds, screen, lost_sound)
				running = False
			obj.y += speed*2
		timer += 1
		seconds = timer // 60
		game_utils.movements(player, WIN_WIDTH, WIN_HEIGHT, speed)
		draw(seconds, obj_rect)
		pygame.display.flip()
	pygame.quit()

if __name__ == "__main__":
	main()