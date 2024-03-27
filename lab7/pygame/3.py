import pygame

pygame.init()

screen_width, screen_height=800, 600
screen = pygame.display.set_mode((screen_width, screen_height))

red = (255, 0, 0)

done = False

clock = pygame.time.Clock()

x = 400
y = 300
radius=25
dx=0
dy=0


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                dx=20 if dx==0 else 0

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]: 
        x += 20
    if keys[pygame.K_LEFT]: 
        x -= 20
    if keys[pygame.K_DOWN]:
        y += 20
    if keys[pygame.K_UP]:
        y -= 20
    
    x+=dx
    y+=dy

    if x-radius<0:
        x=radius
    elif x+radius>screen_width:
        x=screen_width-radius
    
    if y-radius<0:
        y=radius
    elif x+radius>screen_height:
        y=screen_height-radius
        
    screen.fill((255, 255, 255))

    pygame.draw.circle(screen, red, (x,y), radius)
    
    pygame.display.flip()
    clock.tick(60)