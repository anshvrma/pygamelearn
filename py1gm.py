import pygame

pygame.init()

# screen size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# rectangle 
player = pygame.Rect((300, 250, 50, 50))

# loop
run = True
while run:

# screen color
    screen.fill((0, 0, 0))

# rectangle color
    pygame.draw.rect(screen, (255, 0, 0), player)

# controls
    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        player.move_ip(-1, 0)
    if key[pygame.K_d] == True:
        player.move_ip(1, 0)
    if key[pygame.K_w] == True:
        player.move_ip(0, -1)
    if key[pygame.K_s] == True:
        player.move_ip(0, 1)

# event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
