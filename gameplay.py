import pygame
pygame.init()
res = (1440, 740)
screen = pygame.display.set_mode(res)
yellow = (255,255,0)
green = (0, 200, 0)
x = 260
y = 60
n = 0
screen.fill((0,0,20))
square_y = (screen, yellow, (x, y, 50, 50), 0)
square_g = (screen, green, (x, y, 50, 50), 0)
figures = [square_y, square_g]

while(True):
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            exit()
    
    
    #cards = []
    
    if (n <12):
        x = x + 160
        pygame.draw.rect(screen, green, (x, y, 120, 180), 0)
        n = n + 1
        #cards.append(x)
        #cards.append(y)

    if (n ==4 or n == 8):
        y = y + 220
        x = 420
        n = n + 1
        pygame.draw.rect(screen, green, (x, y, 120, 180), 0)
        #cards.append(x)
        #cards.append(y)
    pos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if (420<pos[0]<420+120 and 60<pos[1]<60+180 and click[0]):
        pygame.draw.rect(screen, yellow, (460,120,40,40), 0)

    pygame.display.flip()