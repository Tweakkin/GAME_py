import pygame

def handle_loss(score, screen, lost_sound):
	pygame.mixer.music.stop()
	lost_sound.play()
	font = pygame.font.Font(None, 100)
	font_d = pygame.font.Font(None , 70)
	lose_text = font.render("YOU LOST", 1 , "black")
	score_text = font_d.render(f"Your score is : {score}", 1, "black")
	screen.blit(lose_text, (170, 450))
	screen.blit(score_text, (160, 600))
	pygame.display.flip()
	pygame.time.delay(5000)

def movements(player, WIN_WIDTH, WIN_HEIGHT, speed):
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

def introduction(screen, background, intro_image, clock):
	timer = 0
	intro_running = True
	intro_font = pygame.font.Font(None, 50)
	intro_text = intro_font.render("  PRESS\n  ENTER\nTO START", 1 , "black")
	while intro_running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
		keys_pressed_intro = pygame.key.get_pressed()
		if keys_pressed_intro[pygame.K_RETURN]:
			intro_running = False
		timer += 1
		screen.blit(background, (0, 0))
		screen.blit(intro_image, (100, 250))
		if (timer // 15) % 2 == 0:
			screen.blit(intro_text, (260, 750))
		pygame.display.flip()
		clock.tick(60)
	screen.fill((0, 0, 0))
	pygame.display.flip() 