import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Set up the window
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")

# Load Mickey Mouse image
mickey_image = pygame.image.load("lab7/pygame/mickeyclock.png")
mickey_rect = mickey_image.get_rect(center=(WIDTH // 2, HEIGHT // 2))

# Function to draw clock hands
def draw_hand(surface, angle, length, color, thickness=2):
    end_x = mickey_rect.centerx + length * math.cos(math.radians(angle))
    end_y = mickey_rect.centery - length * math.sin(math.radians(angle))
    pygame.draw.line(surface, color, mickey_rect.center, (end_x, end_y), thickness)

# Main loop
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get current system time
    current_time = pygame.time.get_ticks() // 1000  # Convert to seconds

    # Calculate angles for hands (360 degrees = 60 seconds/minutes)
    seconds_angle = (current_time % 60) * 6
    minutes_angle = (current_time // 60 % 60) * 6

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw Mickey Mouse image
    screen.blit(mickey_image, mickey_rect)

    # Draw clock hands
    draw_hand(screen, seconds_angle, 100, (255, 0, 0), thickness=2)
    draw_hand(screen, minutes_angle, 80, (0, 0, 255), thickness=4)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)
