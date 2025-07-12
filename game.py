import pygame
import random

pygame.init()
WIN_WIDTH = 720
WIN_HEIGHT = 950
screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
lost_sound = pygame.mixer.Sound("game_over.mp3")
background = pygame.image.load("background.jpeg")
pygame.mixer.music.load("game_sound.mp3")
pygame.mixer.music.play(-1) 
PLAYER_WIDTH = 150
PLAYER_HEIGHT = 150
player = pygame.Rect(100, WIN_HEIGHT-(PLAYER_HEIGHT * 2), PLAYER_WIDTH, PLAYER_HEIGHT)
obj_rect = pygame.Rect(random.randint(0, 720), 0, 50, 50)
speed = 5
player_image = pygame.image.load("bird.png").convert_alpha()
rock_image = pygame.image.load("rock_2.png").convert_alpha()
clock = pygame.time.Clock()

def draw(seconds, obj_rect):
	font = pygame.font.Font(None, 70)
	timer_text = font.render(f"{seconds}", 1 , "red")
	screen.blit(background, (0, 0))
	screen.blit(player_image, player)
	screen.blit(timer_text, (360, 150))
	for obj in obj_rect:
		screen.blit(rock_image, obj)

def movements():
	keys_pressed = pygame.key.get_pressed()
	if keys_pressed[pygame.K_LEFT]:
		player.x -= speed
	if keys_pressed[pygame.K_RIGHT]:
		player.x += speed
	if keys_pressed[pygame.K_UP]:
		player.y -= speed
	if keys_pressed[pygame.K_DOWN]:
		player.y += speed
	
	if player.left < 0:
		player.left = 0
	if player.right > WIN_WIDTH:
		player.right = WIN_WIDTH
	if player.top < 0:
		player.top = 0
	if player.bottom > WIN_HEIGHT:
		player.bottom = WIN_HEIGHT

def handle_loss():
	pygame.mixer.music.stop()
	lost_sound.play()
	font = pygame.font.Font(None, 100)
	lose_text = font.render("YOU LOST", 1 , "black")
	screen.blit(lose_text, (170, 450))
	pygame.display.flip()
	pygame.time.delay(5000)

def introduction():
	screen.blit(background, (0, 0))
	


def main():
	#introduction()
	timer = 0
	running = True
	obj_rect = [pygame.Rect(random.randint(0, 720), 0, 50, 50) for _ in range(3)]
	while running:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
		for i in range(len(obj_rect)):
			obj = obj_rect[i]
			if obj.bottom > WIN_HEIGHT:
				obj_rect[i] = pygame.Rect(random.randint(0, 720), 0, 50, 50)
			if player.colliderect(obj):
				handle_loss()
				running = False
			obj.y += speed*2
		timer += 1
		seconds = timer // 60
		movements()
		draw(seconds, obj_rect)
		pygame.display.flip()
	pygame.quit()

if __name__ == "__main__":
	main()