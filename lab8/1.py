import pygame 
import sys 
import random 
import time 
 
from pygame.locals import * 
 
# Initializing 
pygame.init() 
 
# Setting up FPS 
FPS = 60 
FramePerSec = pygame.time.Clock() 
 
# Creating colors 
BLUE = (0, 0, 255) 
RED = (255, 0, 0) 
GREEN = (0, 255, 0) 
BLACK = (0, 0, 0) 
WHITE = (255, 255, 255) 
YELLOW=(255, 255, 0) 
 
# Other Variables for use in the program 
SCREEN_WIDTH = 400 
SCREEN_HEIGHT = 600 
SPEED = 5 
SCORE = 0 
COIN_SCORE = 0  # New variable to keep track of collected coins 
ENEMY_SPEED = SPEED  # Initial enemy speed 
 
# Setting up Fonts 
font = pygame.font.SysFont("Verdana", 60) 
font_small = pygame.font.SysFont("Verdana", 20) 
game_over = font.render("Game Over", True, BLACK) 
 
background = pygame.image.load("lab8/AnimatedStreet.png") 
 
# Create a white screen 
DISPLAYSURF = pygame.display.set_mode((400, 600)) 
DISPLAYSURF.fill(WHITE) 
pygame.display.set_caption("Game") 
 
 
class Coin(pygame.sprite.Sprite):  # New class for coins 
    def __init__(self, weight): 
        super().__init__() 
        self.image = pygame.Surface((20, 20))  # Coin surface 
        self.image.fill(YELLOW)  # Coin color 
        self.rect = self.image.get_rect() 
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0) 
        self.weight = weight  # Assign weight to the coin
 
    def move(self): 
        self.rect.move_ip(0, SPEED) 
        if self.rect.bottom > SCREEN_HEIGHT: 
            self.rect.top = 0 
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0) 
 
 
class Enemy(pygame.sprite.Sprite): 
    def __init__(self): 
        super().__init__() 
        self.image = pygame.image.load("lab8/Enemy.png") 
        self.rect = self.image.get_rect() 
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0) 
 
    def move(self): 
        global SCORE, ENEMY_SPEED  # Access global variable for enemy speed 
        self.rect.move_ip(0, ENEMY_SPEED) 
        if self.rect.bottom > SCREEN_HEIGHT: 
            SCORE += 1 
            self.rect.top = 0 
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0) 
            if SCORE % 10 == 0:  # Increase enemy speed every 10 points
                ENEMY_SPEED += 0.5 
 
 
class Player(pygame.sprite.Sprite): 
    def __init__(self): 
        super().__init__() 
        self.image = pygame.image.load("lab8/Player.png") 
        self.rect = self.image.get_rect() 
        self.rect.center = (160, 520) 
 
    def move(self): 
        pressed_keys = pygame.key.get_pressed() 
        if self.rect.left > 0: 
            if pressed_keys[K_LEFT]: 
                self.rect.move_ip(-5, 0) 
        if self.rect.right < SCREEN_WIDTH: 
            if pressed_keys[K_RIGHT]: 
                self.rect.move_ip(5, 0) 
 
 
# Setting up Sprites 
P1 = Player() 
E1 = Enemy() 
C1 = Coin(random.randint(1, 30))  # Creating a coin sprite with random weight
 
# Creating Sprites Groups 
enemies = pygame.sprite.Group() 
enemies.add(E1) 
coins = pygame.sprite.Group(C1)  # Creating a group for coins 
all_sprites = pygame.sprite.Group() 
all_sprites.add(P1) 
all_sprites.add(E1) 
all_sprites.add(C1)  # Adding coin sprite to all_sprites group 
 
# Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1 
pygame.time.set_timer(INC_SPEED, 1000) 
 
# Game Loop 
while True: 
 
    # Cycles through all events occurring 
    for event in pygame.event.get(): 
        if event.type == INC_SPEED: 
            SPEED += 0.5 
        if event.type == QUIT: 
            pygame.quit() 
            sys.exit() 
 
    DISPLAYSURF.blit(background, (0, 0)) 
    scores = font_small.render("SCORE: " + str(SCORE), True, BLACK) 
    coin_scores = font_small.render("COINS: " + str(COIN_SCORE), True, BLACK)  # Rendering coin score 
    DISPLAYSURF.blit(scores, (10, 10)) 
    DISPLAYSURF.blit(coin_scores, (300, 10))  # Displaying coin score 
 
    # Moves and Re-draws all Sprites 
    for entity in all_sprites: 
        entity.move() 
        DISPLAYSURF.blit(entity.image, entity.rect) 
 
    # To be run if collision occurs between Player and Enemy 
    if pygame.sprite.spritecollideany(P1, enemies): 
        pygame.mixer.Sound('lab8/crash.wav').play() 
        time.sleep(1) 
 
        DISPLAYSURF.fill(RED) 
        DISPLAYSURF.blit(game_over, (30, 250)) 
 
        pygame.display.update() 
        for entity in all_sprites: 
            entity.kill() 
        time.sleep(2)
        pygame.quit() 
        sys.exit() 
 
    # Check if Player collects a coin 
    collected_coin = pygame.sprite.spritecollideany(P1, coins) 
    if collected_coin: 
        COIN_SCORE += collected_coin.weight  # Increase coin score by the weight of the collected coin
        collected_coin.kill()  # Remove the coin sprite when collected 
 
    pygame.display.update() 
    FramePerSec.tick(FPS)
