import pygame
import pygame.freetype
import random
 

pygame.init()
res = (1440, 740)
screen = pygame.display.set_mode(res)
image = pygame.image.load("shuffle.png")
my_font = pygame.freetype.Font("NotoSans-Regular.ttf", 24)
yellow = (255,255,0)
white = (255,255,255)
green = (0, 200, 0)
score = 0
cores = [(200,0,0), (200,200,200), (0,0,200), (200,200,0), (0,200,200), (150,50,200)]


def lvl1():
    x = 420
    y = 60
    i = 0
    baralhar = [0,0,1,1,2,2,3,3,4,4,5,5]

    screen.fill((0,0,20))
    random.shuffle(baralhar)

    #desenha as cartas
    cardpos = []

    cardpos.append(pygame.Rect(420, 60, 120, 180))
    for a in range(12):
        pygame.draw.rect(screen, green, (x, y, 120, 180), 0)
        x = x + 160
        
        if (a == 3 or a == 7):
            y = y + 220
            x = 260
            x = x + 160

        m_rect = pygame.Rect(x,y, 120, 180)
        cardpos.append(m_rect)
 
    while(True):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                exit()
            pos = pygame.mouse.get_pos()
            for card in cardpos:
                if card.collidepoint(pos) and i<12:
                    if(event.type == pygame.MOUSEBUTTONUP):
                        cardpos.remove(card)
                        pygame.draw.rect(screen, cores[baralhar[i]], card, 0)
                        i+=1
                        
    
        #desenha botão exit
        pygame.draw.rect(screen, yellow, (50,650,140,30), 2)
        my_font.render_to(screen, (100,655), "Exit", yellow)
        #desenha o score
        my_font.render_to(screen, (50,50), "Score: " + str(score), yellow)
        pos = pygame.mouse.get_pos()
        #coisas brancaas?

        #botão exit    
        if(50<pos[0]<50+140 and 650<pos[1]<650+30):
            pygame.draw.rect(screen, white, (50,650,140,30), 2)
            my_font.render_to(screen, (100,655), "Exit", white)
       
        pygame.display.flip()
        
        #voltar ao menu
        if(50<pos[0]<50+140 and 650<pos[1]<650+30):
            if(event.type == pygame.MOUSEBUTTONUP):
                exit()
                
lvl1()