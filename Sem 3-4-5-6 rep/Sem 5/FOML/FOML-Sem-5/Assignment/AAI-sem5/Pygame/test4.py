import pygame
import sys

pygame.init()

# Constants
width, height = 1000, 600
cell_size = 30
wall_color = (0, 0, 255)  # Blue color for walls

# Define the maze layout using a 2D array
# maze_layout = [
#     "####################",
#     "#..................#",
#     "#..##..............#",
#     "#..................#",
#     "#.####.#####.#.###.#",
#     "#.#  #.#   #.#.#   #",
#     "#.#  #.#.# #.#.# #.#",
#     "#.####.#.# #.#.# #.#",
#     "#......#.#   #   #.#",
#     "####################",
# ]

# maze_layout = [
#     "###############################################",
#     "#.............................................#",
#     "#.............................................#",
#     "#..###..###..#####..###..#####..#..##..##..#..#",
#     "#..#",
#     "#..###.."
# ]

maze_layout = [
    "#######################",
    "#..........#..........#",
    "#..........#..........#",
    "#..##..##..#..##..##..#",
    "#.....................#",
    "#..##..#..###..#..##..#",
    "#......##..#..##......#",
    "###....#...#...#..#####",
    "#.....................#",
    "#......#..............#",
    "#......#..............#",
    "#.....................#",
    "#.....................#",
    "#######################"    
]

# Initialize the screen
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pac-Man Walls")

# Function to draw the maze
def draw_maze():
    for row in range(len(maze_layout)):
        for col in range(len(maze_layout[row])):
            x = col * cell_size
            y = row * cell_size
            if maze_layout[row][col] == "#":
                pygame.draw.rect(screen, wall_color, (x, y, cell_size, cell_size))

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  # Clear the screen
    draw_maze()  # Draw the maze walls
    pygame.display.flip()  # Update the display

pygame.quit()
sys.exit()
