import pygame, sys, math
pygame.init()

length_screen = 1500
width_screen = 770
wall_vert = 1050
wall_hor = 1400

screen = pygame.display.set_mode((length_screen, width_screen), pygame.RESIZABLE)
pygame.display.set_caption('Hello')

origin_x = length_screen / 2
origin_y = width_screen / 2
speed = 2

collision = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and origin_x > 0 and not collision:
        origin_x -= speed
    if keys[pygame.K_RIGHT] and origin_x < length_screen - 50 and not collision:
        origin_x += speed
    if keys[pygame.K_UP] and origin_y > 0 and not collision:
        origin_y -= speed
    if keys[pygame.K_DOWN] and origin_y < width_screen - 50 and not collision:
        origin_y += speed

    # Calculate distance between center of circle and line
    circle_center = (origin_x, origin_y)
    line_start = (25, 25)
    line_end = (1000, 25)
    
    # Use the formula for the distance between a point and a line
    distance = abs((line_end[1] - line_start[1]) * circle_center[0] - (line_end[0] - line_start[0]) * circle_center[1] + line_end[0] * line_start[1] - line_end[1] * line_start[0]) / math.sqrt((line_end[1] - line_start[1]) ** 2 + (line_end[0] - line_start[0]) ** 2)

    # Check for collision
    circle_radius = 50
    line_width = 10
    if distance <= (circle_radius + line_width+0.25 / 2):
        collision = True
    else:
        collision = False

    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, color=(255, 120, 0), center=(origin_x, origin_y), radius=50)
    pygame.draw.line(screen, color=(0, 0, 220), start_pos=(25, 25), end_pos=(1000, 25), width=10)

    # Handle collision

    pygame.display.update()
