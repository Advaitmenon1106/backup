import pygame
import sys

pygame.init()

length_screen = 1500
width_screen = 800

# Constants
width, height = 1500, 800
cell_size = 30
wall_color = (0, 0, 255)

maze_layout = [
    "#######################",
    "#..........#..........#",
    "#..........#..........#",
    "#..##..##..#..##..##..#",
    "#.....................#",
    "#.....................#",
    "#..##..#..###..#..##..#",
    "#..##..#...#...#..##..#",
    "#......##..#..##......#",
    "#......##..#..##......#",
    "###....#...#...#..#####",
    "#......#.......#......#",
    "#.....................#",
    "#.....................#",
    "#......#.......#......#",
    "#......#.......#......#",
    "#.....................#",
    "#.....................#",
    "#######################"    
]

# Initialize the screen
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
pygame.display.set_caption("Pac-Man")

origin_x = 60
origin_y = 60
speed = 0.5

# Function to draw the maze
def draw_maze():
    for row in range(len(maze_layout)):
        for col in range(len(maze_layout[row])):
            x = col * cell_size
            y = row * cell_size
            if maze_layout[row][col] == "#":
                pygame.draw.rect(screen, wall_color, (x, y, cell_size, cell_size))

def check_collisions(x, y, direction):
    row = int(y / cell_size)
    col = int(x / cell_size)

    if direction == "left":
        if col > 0 and maze_layout[row][col - 1] != "#":
            return False
    elif direction == "right":
        if col < len(maze_layout[0]) - 1 and maze_layout[row][col + 1] != "#":
            return False
    elif direction == "up":
        if row > 0 and maze_layout[row - 1][col] != "#":
            return False
    elif direction == "down":
        if row < len(maze_layout) - 1 and maze_layout[row + 1][col] != "#":
            return False

    return True

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get Pac-Man's potential new position
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

    screen.fill((0, 0, 0))

    pygame.draw.circle(screen, color=(253, 255, 0), center=(origin_x, origin_y), radius=25)
    draw_maze()

    pygame.display.flip()  # Update the display
