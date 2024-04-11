import pygame 
from datetime import datetime as dt 
 
pygame.init() 
screen = pygame.display.set_mode((620 , 620)) 
pygame.display.set_caption("mickey mouse watch") 
suret = pygame.image.load("lab7/pygame/body.png") 
suret = pygame.transform.scale(suret, (620, 620))  
suret2 = pygame.image.load("lab7/pygame/left_hand.png") 
suret2 = pygame.transform.scale(suret2, (50,150))  
suret3 = pygame.image.load("lab7/pygame/right_hand.png") 
suret3 = pygame.transform.scale(suret3, (50,150))  
clock = pygame.time.Clock() 
 
running = True 
while running: 
    screen.fill((255,255,255)) 
    screen.blit(suret, (0, 0))  # Установка позиции тела Микки Мауса
 
    current_time = dt.now().time() 
 
    seconds_angle = -(current_time.second * 6) 
    minutes_angle = -(current_time.minute * 6) 
 
    rotated_leftarm = pygame.transform.rotate(suret2, minutes_angle)  # Минуты
    rotated_rightarm = pygame.transform.rotate(suret3, seconds_angle)  # Секунды
 
    leftarm_rect = rotated_leftarm.get_rect(center=(310, 310)) 
    rightarm_rect = rotated_rightarm.get_rect(center=(310, 310))  # Исправлены координаты для центрирования
 
    screen.blit(rotated_leftarm, (310 - leftarm_rect.width / 2, 310 - leftarm_rect.height / 2))  # Один конец руки в центре
    screen.blit(rotated_rightarm, (310 - rightarm_rect.width / 2, 310 - rightarm_rect.height / 2))  # Один конец руки в центре
 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False 
 
    pygame.display.update() 
    clock.tick(60) 
 
pygame.quit()
