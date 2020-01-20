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




def lvl1():
    x = 420
    y = 60
    baralhar = [0,0,1,1,2,2,3,3,4,4,5,5]
    cores = [(200,0,0), (200,200,200), (0,0,200), (200,200,0), (0,200,200), (150,50,200)]
    cardpos = []
    cardcolor = []
    cartasreveladas = []
    cartasreveladaspos = []
    numero_reveladas = 0
    win = 0
    score = 0
    s = 0
    

    screen.fill((0,0,20))
    random.shuffle(baralhar)
    
    #desenha as cartas

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
    
    

    for j in range(len(baralhar)):
        cardcolor.append(cores[baralhar[j]])
    
    

    while(True):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                exit()
            pos = pygame.mouse.get_pos()
            if(event.type == pygame.MOUSEBUTTONUP):
                for i in range(len(cardpos)):
                    if (cardpos[i][0]<pos[0]<cardpos[i][0]+120 and cardpos[i][1]<pos[1]<cardpos[i][1]+180):
                        cartasreveladas.append(cardcolor[i])
                        cartasreveladaspos.append(cardpos[i])
                        print(cartasreveladaspos)
                        pygame.draw.rect(screen, cardcolor[i], cardpos[i], 0)
                        numero_reveladas+=1
                        pygame.display.flip()
                        if(numero_reveladas == 2):
                            pygame.time.wait(1000)
                            if(cartasreveladas[0]==cartasreveladas[1] and cartasreveladaspos[0]!=cartasreveladaspos[1]):
                                cardpos[i] = pygame.Rect(0,0,0,0)
                                cardpos[i] = pygame.Rect(0,0,0,0)          
                                cartasreveladas.pop(1)
                                cartasreveladas.pop(0)
                                cartasreveladaspos.pop(1)
                                cartasreveladaspos.pop(0)
                                numero_reveladas = 0
                                win+=1
                                score+=100
                                pygame.draw.rect(screen, (0,0,20), (50,50,200,200), 0)
                                s = 0

                            else:
                                pygame.draw.rect(screen, green, cartasreveladaspos[0], 0)
                                pygame.draw.rect(screen, green, cartasreveladaspos[1], 0)
                                cartasreveladas.pop(1)
                                cartasreveladas.pop(0)
                                cartasreveladaspos.pop(1)
                                cartasreveladaspos.pop(0)
                                numero_reveladas = 0
                                if(score<0):
                                    score = 0
                                if(score>0):
                                    score-=20*s
                                    s+=1
                                    pygame.draw.rect(screen, (0,0,20), (50,50,200,200), 0)

            if(win==6):
                screen.fill((0,0,20))
                my_font.render_to(screen, (640,370), "Congratulations!!!", white)
                
                        
    
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
    x = 420
    y = 60
    baralhar = [0,0,1,1,2,2,3,3,4,4,5,5,6,6,7,7]
    cores = [(200,0,0), (200,200,200), (0,0,200), (200,200,0), (0,200,200), (150,50,200), (200,0,200), (92,51,23)]
    cardpos = []
    cardcolor = []
    cartasreveladas = []
    cartasreveladaspos = []
    numero_reveladas = 0
    win = 0
    score = 0
    s = 0
    

    screen.fill((0,0,20))
    random.shuffle(baralhar)
    
    
    #desenha as cartas

    cardpos.append(pygame.Rect(420, 60, 120, 140))
    for a in range(16):
        pygame.draw.rect(screen, green, (x, y, 120, 140), 0)
        x = x + 160
        
        if (a == 3 or a == 7 or a == 11):
            y = y + 160
            x = 260
            x = x + 160

        m_rect = pygame.Rect(x,y, 120, 140)
        cardpos.append(m_rect)
    
    

    for j in range(len(baralhar)):
        cardcolor.append(cores[baralhar[j]])
    
    

    while(True):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                exit()
            pos = pygame.mouse.get_pos()
            if(event.type == pygame.MOUSEBUTTONUP):
                for i in range(len(cardpos)):
                    if (cardpos[i][0]<pos[0]<cardpos[i][0]+120 and cardpos[i][1]<pos[1]<cardpos[i][1]+140):
                        cartasreveladas.append(cardcolor[i])
                        cartasreveladaspos.append(cardpos[i])
                        print(cartasreveladaspos)
                        pygame.draw.rect(screen, cardcolor[i], cardpos[i], 0)
                        numero_reveladas+=1
                        pygame.display.flip()
                        if(numero_reveladas == 2):
                            pygame.time.wait(1000)
                            if(cartasreveladas[0]==cartasreveladas[1] and cartasreveladaspos[0]!=cartasreveladaspos[1]):
                                cardpos[i] = pygame.Rect(0,0,0,0)
                                cardpos[i] = pygame.Rect(0,0,0,0)          
                                cartasreveladas.pop(1)
                                cartasreveladas.pop(0)
                                cartasreveladaspos.pop(1)
                                cartasreveladaspos.pop(0)
                                numero_reveladas = 0
                                win+=1
                                score+=100
                                pygame.draw.rect(screen, (0,0,20), (50,50,200,200), 0)
                                s = 0

                            else:
                                pygame.draw.rect(screen, green, cartasreveladaspos[0], 0)
                                pygame.draw.rect(screen, green, cartasreveladaspos[1], 0)
                                cartasreveladas.pop(1)
                                cartasreveladas.pop(0)
                                cartasreveladaspos.pop(1)
                                cartasreveladaspos.pop(0)
                                numero_reveladas = 0
                                if(score<0):
                                    score = 0
                                if(score>0):
                                    score-=20*s
                                    s+=1
                                    pygame.draw.rect(screen, (0,0,20), (50,50,200,200), 0)

            if(win==8):
                screen.fill((0,0,20))
                my_font.render_to(screen, (640,370), "Congratulations!!!", white)

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
 
def lvl3():
    x = 400
    y = 60
    baralhar = [0,0,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9]
    cores = [(200,0,0), (200,200,200), (0,0,200), (200,200,0), (0,200,200), (150,50,200), (200,0,200), (92,51,23), (33,94,33), (0,20,0)]
    cardpos = []
    cardcolor = []
    cartasreveladas = []
    cartasreveladaspos = []
    numero_reveladas = 0
    win = 0
    score = 0
    s = 0
    

    screen.fill((0,0,20))
    random.shuffle(baralhar)
    
    
    #desenha as cartas

    cardpos.append(pygame.Rect(400, 60, 120, 140))
    for a in range(20):
        pygame.draw.rect(screen, green, (x, y, 120, 140), 0)
        x = x + 160
        
        if (a == 4 or a == 9 or a == 14):
            y = y + 160
            x = 400
            

        m_rect = pygame.Rect(x,y, 120, 140)
        cardpos.append(m_rect)
    
    

    for j in range(len(baralhar)):
        cardcolor.append(cores[baralhar[j]])
    
    

    while(True):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                exit()
            pos = pygame.mouse.get_pos()
            if(event.type == pygame.MOUSEBUTTONUP):
                for i in range(len(cardpos)):
                    if (cardpos[i][0]<pos[0]<cardpos[i][0]+120 and cardpos[i][1]<pos[1]<cardpos[i][1]+140):
                        cartasreveladas.append(cardcolor[i])
                        cartasreveladaspos.append(cardpos[i])
                        print(cartasreveladaspos)
                        pygame.draw.rect(screen, cardcolor[i], cardpos[i], 0)
                        numero_reveladas+=1
                        pygame.display.flip()
                        if(numero_reveladas == 2):
                            pygame.time.wait(1000)
                            if(cartasreveladas[0]==cartasreveladas[1] and cartasreveladaspos[0]!=cartasreveladaspos[1]):
                                cardpos[i] = pygame.Rect(0,0,0,0)
                                cardpos[i] = pygame.Rect(0,0,0,0)          
                                cartasreveladas.pop(1)
                                cartasreveladas.pop(0)
                                cartasreveladaspos.pop(1)
                                cartasreveladaspos.pop(0)
                                numero_reveladas = 0
                                win+=1
                                score+=100
                                pygame.draw.rect(screen, (0,0,20), (50,50,200,200), 0)
                                s = 0

                            else:
                                pygame.draw.rect(screen, green, cartasreveladaspos[0], 0)
                                pygame.draw.rect(screen, green, cartasreveladaspos[1], 0)
                                cartasreveladas.pop(1)
                                cartasreveladas.pop(0)
                                cartasreveladaspos.pop(1)
                                cartasreveladaspos.pop(0)
                                numero_reveladas = 0
                                if(score<0):
                                    score = 0
                                if(score>0):
                                    score-=20*s
                                    s+=1
                                    pygame.draw.rect(screen, (0,0,20), (50,50,200,200), 0)

            if(win==10):
                screen.fill((0,0,20))
                my_font.render_to(screen, (640,370), "Congratulations!!!", white)

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

def lvl4():
    x = 380
    y = 60
    baralhar = [0,0,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,11,11,12,12,13,13,14,14]
    cores = [(200,0,0), (200,200,200), (0,0,200), (200,200,0), (0,200,200), (150,50,200), (200,0,200), (92,51,23), (33,94,33), (0,20,0), (255,165,0), (0,0,0), (89,89,171), (140,120,83), (143,143,189)]
    cardpos = []
    cardcolor = []
    cartasreveladas = []
    cartasreveladaspos = []
    numero_reveladas = 0
    win = 0
    score = 0
    s = 0
    

    screen.fill((0,0,20))
    random.shuffle(baralhar)
    
    
    #desenha as cartas

    cardpos.append(pygame.Rect(380, 60, 80, 100))
    for a in range(30):
        pygame.draw.rect(screen, green, (x, y, 80, 100), 0)
        x = x + 120
        
        if (a == 5 or a == 11 or a == 17 or a == 23):
            y = y + 120
            x = 380
            

        m_rect = pygame.Rect(x,y, 80, 100)
        cardpos.append(m_rect)
    
    

    for j in range(len(baralhar)):
        cardcolor.append(cores[baralhar[j]])
    
    

    while(True):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                exit()
            pos = pygame.mouse.get_pos()
            if(event.type == pygame.MOUSEBUTTONUP):
                for i in range(len(cardpos)):
                    if (cardpos[i][0]<pos[0]<cardpos[i][0]+80 and cardpos[i][1]<pos[1]<cardpos[i][1]+100):
                        cartasreveladas.append(cardcolor[i])
                        cartasreveladaspos.append(cardpos[i])
                        print(cartasreveladaspos)
                        pygame.draw.rect(screen, cardcolor[i], cardpos[i], 0)
                        numero_reveladas+=1
                        pygame.display.flip()
                        if(numero_reveladas == 2):
                            pygame.time.wait(1000)
                            if(cartasreveladas[0]==cartasreveladas[1] and cartasreveladaspos[0]!=cartasreveladaspos[1]):
                                cardpos[i] = pygame.Rect(0,0,0,0)
                                cardpos[i] = pygame.Rect(0,0,0,0)          
                                cartasreveladas.pop(1)
                                cartasreveladas.pop(0)
                                cartasreveladaspos.pop(1)
                                cartasreveladaspos.pop(0)
                                numero_reveladas = 0
                                win+=1
                                score+=100
                                pygame.draw.rect(screen, (0,0,20), (50,50,200,200), 0)
                                s = 0

                            else:
                                pygame.draw.rect(screen, green, cartasreveladaspos[0], 0)
                                pygame.draw.rect(screen, green, cartasreveladaspos[1], 0)
                                cartasreveladas.pop(1)
                                cartasreveladas.pop(0)
                                cartasreveladaspos.pop(1)
                                cartasreveladaspos.pop(0)
                                numero_reveladas = 0
                                if(score<0):
                                    score = 0
                                if(score>0):
                                    score-=20*s
                                    s+=1
                                    pygame.draw.rect(screen, (0,0,20), (50,50,200,200), 0)

            if(win==15):
                screen.fill((0,0,20))
                my_font.render_to(screen, (640,370), "Congratulations!!!", white)

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


def lvl5():
    screen.fill((0,0,20))
    while(True):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                exit()
        my_font.render_to(screen, (640,370), "Coming soon...", white)
        #desenha botão exit
        pygame.draw.rect(screen, yellow, (50,650,140,30), 2)
        my_font.render_to(screen, (100,655), "Exit", yellow)
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

        if(650<pos[0]<650+140 and 370<pos[1]<370+40+30):
            if(event.type == pygame.MOUSEBUTTONUP):
                lvl3()

        if(650<pos[0]<650+140 and 370<pos[1]<370+80+30):
            if(event.type == pygame.MOUSEBUTTONUP):
                lvl4()

        if(650<pos[0]<650+140 and 370<pos[1]<370+120+30):
            if(event.type == pygame.MOUSEBUTTONUP):
                lvl5()

        pygame.time.wait(5)
main()