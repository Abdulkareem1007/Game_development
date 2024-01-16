# Import the necessary Pygame modules
import pygame
import sys

# Initialize Pygame
pygame.init()

# Define the screen dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Game variables
gravity = 0.25
bird_movement = 0
game_active = True

# Load images
bird_surface = pygame.image.load('assets/bluebird-midflap.png').convert_alpha()
bird_rect = bird_surface.get_rect(center=(100, SCREEN_HEIGHT // 2))

# Game loop
while True:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                bird_movement = 0
                bird_movement -= 6

    # Bird movement
    bird_movement += gravity
    bird_rect.centery += bird_movement

    # Draw the background
    screen.fill(WHITE)

    # Draw the bird
    screen.blit(bird_surface, bird_rect)

    # Update the display
    pygame.display.update()

    # Frame rate
    pygame.time.Clock().tick(120)

this is the code generate readme file for github
