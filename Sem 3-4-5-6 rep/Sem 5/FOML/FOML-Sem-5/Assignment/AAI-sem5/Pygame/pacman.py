import pygame, sys

pygame.init()

length_screen = 1500
width_screen = 770

screen = pygame.display.set_mode((length_screen, width_screen), pygame.RESIZABLE)
origin_x = length_screen / 2
origin_y = width_screen / 2
speed = 0.5
circle = pygame.draw.circle(screen, color=(255, 120, 0), center=(origin_x, origin_y), radius=25)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and origin_x > 0:
            origin_x -= speed
    if keys[pygame.K_RIGHT] and origin_x < length_screen - 50:
            origin_x += speed
    if keys[pygame.K_UP] and origin_y > 0:
            origin_y -= speed
    if keys[pygame.K_DOWN] and origin_y < width_screen - 50:
            origin_y += speed
        
    screen.fill((0, 0, 0))
        
    pygame.draw.circle(screen, color=(253,255,0), center=(origin_x, origin_y), radius=25)
    pygame.display.update()
