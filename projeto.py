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
                main()
 
def lvl2():
    screen.fill((0,0,20))
    while(True):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                exit()
        #desenha botão exit
        pygame.draw.rect(screen, yellow, (50,650,140,30), 2)
        my_font.render_to(screen, (100,655), "Exit", yellow)
        #desenha o score
        my_font.render_to(screen, (50,50), "Score: " + str(score), yellow)
        pos = pygame.mouse.get_pos()
       
        if(50<pos[0]<50+140 and 650<pos[1]<650+30):
            pygame.draw.rect(screen, white, (50,650,140,30), 2)
            my_font.render_to(screen, (100,655), "Exit", white)
       
        pygame.display.flip()
        #voltar ao menu
        if(50<pos[0]<50+140 and 650<pos[1]<650+30):
            if(event.type == pygame.MOUSEBUTTONUP):
                main()
 
def main():
    while(True):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                exit()
        screen.fill((0,0,20))
        #desenha o menu
        y = 330
        for i in range(5):
            pygame.draw.rect(screen, yellow, (650,y,140,30), 2)
            y = y + 40
       
        pygame.draw.rect(screen, yellow, (650,370+180,140,30), 2)
       
        screen.blit(image, ((740/2)-35,0))
       
        my_font.render_to(screen, (700,370-35), "4x3", yellow)
        my_font.render_to(screen, (700,370+5), "4x4", yellow)
        my_font.render_to(screen, (700,370+45), "5x4", yellow)
        my_font.render_to(screen, (700,370+85), "6x5", yellow)
        my_font.render_to(screen, (700,370+125), "6x6", yellow)
        my_font.render_to(screen, (700,370+185), "Exit", yellow)
        #muda as cores do menu de amarelo para branco
        pos = pygame.mouse.get_pos()
        if(650<pos[0]<650+140 and 370-40<pos[1]<370-40+30):
            pygame.draw.rect(screen, white, (650,370-40,140,30), 2)
            my_font.render_to(screen, (700,370-35), "4x3", white)
        elif(650<pos[0]<650+140 and 370<pos[1]<370+30):
            pygame.draw.rect(screen, white, (650,370,140,30), 2)
            my_font.render_to(screen, (700,370+5), "4x4", white)
        elif(650<pos[0]<650+140 and 370+40<pos[1]<370+40+30):
            pygame.draw.rect(screen, white, (650,370+40,140,30), 2)
            my_font.render_to(screen, (700,370+45), "5x4", white)
        elif(650<pos[0]<650+140 and 370+80<pos[1]<370+80+30):
            pygame.draw.rect(screen, white, (650,370+80,140,30), 2)
            my_font.render_to(screen, (700,370+85), "6x5", white)
        elif(650<pos[0]<650+140 and 370+120<pos[1]<370+120+30):
            pygame.draw.rect(screen, white, (650,370+120,140,30), 2)
            my_font.render_to(screen, (700,370+125), "6x6", white)
        elif(650<pos[0]<650+140 and 370+180<pos[1]<370+180+30):
            pygame.draw.rect(screen, white, (650,370+180,140,30), 2)
            my_font.render_to(screen, (700,370+185), "Exit", white)
        pygame.display.flip()
        #sair do jogo
        if(650<pos[0]<650+140 and 370+180<pos[1]<370+180+30):
            if(event.type == pygame.MOUSEBUTTONUP):
                exit()
        #Nivel 1
        if(650<pos[0]<650+140 and 370-40<pos[1]<370-40+30):
            if(event.type == pygame.MOUSEBUTTONUP):
                lvl1()
        #Nivel 2
        if(650<pos[0]<650+140 and 370<pos[1]<370+30):
            if(event.type == pygame.MOUSEBUTTONUP):
                lvl2()
        pygame.time.wait(5)
main()