import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
window_width = 800
window_height = 600
wordle_word = "APPLE"  # Replace with your secret word
max_attempts = 6

# Colors
white = (255, 255, 255)

# Set up the window
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Wordle")

# Initialize game variables
attempts = 0
guessed_word = ["_"] * len(wordle_word)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and attempts < max_attempts:
            if event.key >= 97 and event.key <= 122:  # Check if the key is a lowercase letter
                letter = chr(event.key).upper()
                if letter not in guessed_word:
                    if letter in wordle_word:
                        indices = [i for i, char in enumerate(wordle_word) if char == letter]
                        for index in indices:
                            guessed_word[index] = letter
                    attempts += 1

    window.fill(white)

    # Display the guessed word
    font = pygame.font.Font(None, 48)
    text = font.render(" ".join(guessed_word), True, (0, 0, 0))
    window.blit(text, (10, 10))

    # Display remaining attempts
    attempts_text = f"Attempts: {attempts}/{max_attempts}"
    attempts_render = font.render(attempts_text, True, (0, 0, 0))
    window.blit(attempts_render, (10, 70))

    if attempts >= max_attempts:
        # Game over message
        game_over_text = font.render("Game Over! The word was: " + wordle_word, True, (255, 0, 0))
        window.blit(game_over_text, (10, 130))

    if "_" not in guessed_word:
        # Victory message
        victory_text = font.render("Congratulations! You guessed the word!", True, (0, 255, 0))
        window.blit(victory_text, (10, 130))

    pygame.display.update()

# Quit Pygame
pygame.quit()
