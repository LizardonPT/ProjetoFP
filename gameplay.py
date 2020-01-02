import pygame
pygame.init()
res = (1440, 740)
screen = pygame.display.set_mode(res)
green = (0, 200, 0)
x = 260
y = 60
n = 0
screen.fill((0,0,20))

while(True):
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            exit()
    
    if (n <12):
        x = x + 160
        pygame.draw.rect(screen, green, (x, y, 120, 180), 0)
        n = n + 1

    if (n ==4 or n == 8):
        y = y + 220
        x = 420
        n = n + 1
        pygame.draw.rect(screen, green, (x, y, 120, 180), 0)
    

    pygame.display.flip()