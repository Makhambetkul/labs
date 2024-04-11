import pygame 
import random 
from color_palette import *  # Assuming color_palette contains the color constants 
 
pygame.init() 
 
WIDTH = 600 
HEIGHT = 600 
CELL = 30 
 
def draw_grid(): 
    for i in range(HEIGHT // 2): 
        for j in range(WIDTH // 2): 
            pygame.draw.rect(screen, colorGRAY, (i * CELL, j * CELL, CELL, CELL), 1) 
 
def draw_grid_chess(): 
    colors = [colorWHITE, colorGRAY] 
    for i in range(HEIGHT // 2): 
        for j in range(WIDTH // 2): 
            pygame.draw.rect(screen, colors[(i + j) % 2], (i * CELL, j * CELL, CELL, CELL)) 
 
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Corrected the order of arguments 
 
class Point: 
    def __init__(self, x, y): 
        self.x = x 
        self.y = y 
 
    def __str__(self): 
        return f"{self.x}, {self.y}" 
 
class Snake: 
    def __init__(self): 
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)] 
        self.dx = 1 
        self.dy = 0 
 
    def move(self): 
        for i in range(len(self.body) - 1, 0, -1): 
            self.body[i].x = self.body[i - 1].x 
            self.body[i].y = self.body[i - 1].y 
        self.body[0].x += self.dx 
        self.body[0].y += self.dy 
 
    def draw(self): 
        head = self.body[0] 
        pygame.draw.rect(screen, colorRED, (head.x * CELL, head.y * CELL, CELL, CELL)) 
        for segment in self.body[1:]: 
            pygame.draw.rect(screen, colorYELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL)) 
 
    def check_collision(self, food): 
        head = self.body[0] 
        if head.x == food.pos.x and head.y == food.pos.y: 
            self.body.append(Point(head.x, head.y)) 
            return food.weight  # Return the weight of the food 
        return 0  # Return 0 if no collision 
 
    def check_border_collision(self): 
        head = self.body[0] 
        if head.x < 0 or head.x >= WIDTH / CELL or head.y < 0 or head.y >= HEIGHT / CELL: 
            return True 
        return False 
 
class Food: 
    def __init__(self): 
        self.pos = Point(9, 9) 
        self.weight = random.randint(1, 3)  # Assign a random weight to the food 
        self.timer = 100  # Initial timer value for food (adjust as needed)
 
    def generate_position(self): 
        self.pos = Point(random.randint(0, WIDTH // CELL - 1), random.randint(0, HEIGHT // CELL - 1)) 
        self.weight = random.randint(1, 3)  # Assign a new random weight to the food 
        self.timer = 100  # Reset timer when regenerating food 
 
    def draw(self): 
        pygame.draw.rect(screen, colorGREEN, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL)) 
 
    def decrease_timer(self): 
        self.timer -= 1  # Decrease timer value each frame 
        if self.timer <= 0: 
            self.generate_position()  # Regenerate food when timer runs out 
 
FPS = 5 
clock = pygame.time.Clock() 
 
food = Food() 
snake = Snake() 
 
score = 0 
level = 1 
foods_eaten = 0 
speed_increment = 0.5 
 
font = pygame.font.Font(None, 36) 
 
done = False 
while not done: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True 
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_RIGHT: 
                snake.dx = 1 
                snake.dy = 0 
            elif event.key == pygame.K_LEFT: 
                snake.dx = -1 
                snake.dy = 0 
            elif event.key == pygame.K_DOWN: 
                snake.dx = 0 
                snake.dy = 1 
            elif event.key == pygame.K_UP: 
                snake.dx = 0 
                snake.dy = -1 
 
    draw_grid_chess() 
 
    snake.move() 
 
    if snake.check_border_collision():  # Check for border collision 
        # Game over handling 
        print("Game Over!") 
        done = True 
 
    food.decrease_timer()  # Decrease timer for food 
    snake_collision = snake.check_collision(food) 
    if snake_collision > 0: 
        foods_eaten += 1 
        score += snake_collision 
        if foods_eaten == 3 or score >= 40:  # Increase speed and level 
            level += 1
            FPS += speed_increment 
            foods_eaten = 0 
            speed_increment += 0.5 
            print(f"Level: {level}") 
        food.generate_position()  # Generate new position for food 
 
    snake.draw() 
    food.draw() 
 
    # Show score and level on the screen 
    score_text = font.render(f"Score: {score}", True, colorBLACK) 
    level_text = font.render(f"Level: {level}", True, colorBLACK) 
    screen.blit(score_text, (10, 10)) 
    screen.blit(level_text, (10, 50)) 
    pygame.display.flip() 
    clock.tick(FPS)
