    new_x = origin_x
    new_y = origin_y

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and origin_x > 0:
        new_x -= speed
        if check_collisions(new_x, new_y, "left"):
            new_x = origin_x
    if keys[pygame.K_RIGHT] and origin_x < length_screen - 50:
        new_x += speed
        if check_collisions(new_x, new_y, "right"):
            new_x = origin_x
    if keys[pygame.K_UP] and origin_y > 0:
        new_y -= speed
        if check_collisions(new_x, new_y, "up"):
            new_y = origin_y
    if keys[pygame.K_DOWN] and origin_y < width_screen - 50:
        new_y += speed
        if check_collisions(new_x, new_y, "down"):
            new_y = origin_y

    # Update Pac-Man's position
    origin_x = new_x
    origin_y = new_y