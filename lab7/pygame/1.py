import pygame
import sys
import math

pygame.init()

WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")


mickey_image = pygame.image.load("lab7/pygame/mickeyclock.png")
mickey_rect = mickey_image.get_rect(center=(WIDTH // 2, HEIGHT // 2))


clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    
    current_time = pygame.time.get_ticks() // 1000  

    
    seconds_angle = (current_time % 60) * 6
    minutes_angle = (current_time // 60 % 60) * 6

    
    screen.fill((255, 255, 255))

    
    screen.blit(mickey_image, mickey_rect)

    
    pygame.draw.line(screen, (255, 0, 0), mickey_rect.center,
                     (mickey_rect.centerx + 100 * math.cos(math.radians(seconds_angle)),
                      mickey_rect.centery - 100 * math.sin(math.radians(seconds_angle))), 2)
    pygame.draw.line(screen, (0, 0, 255), mickey_rect.center,
                     (mickey_rect.centerx + 80 * math.cos(math.radians(minutes_angle)),
                      mickey_rect.centery - 80 * math.sin(math.radians(minutes_angle))), 4)

    
    pygame.display.flip()

    
    clock.tick(60)
