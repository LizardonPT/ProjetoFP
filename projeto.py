import pygame
import pygame.freetype


pygame.init()
res = (1440, 740)
screen = pygame.display.set_mode(res)
image = pygame.image.load("shuffle.png")
my_font = pygame.freetype.Font("NotoSans-Regular.ttf", 24)
yellow = (255,255,0)
white = (255,255,255)
green = (0, 200, 0)
score = 0

def lvl1():
    x = 260
    y = 60
    n = 0
    screen.fill((0,0,20))
    
    while(True):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                exit()
        #desenha as cartas
        if (n <12):
            x = x + 160
            pygame.draw.rect(screen, green, (x, y, 120, 180), 0)
            n = n + 1

        if (n ==4 or n == 8):
            y = y + 220
            x = 420
            n = n + 1
            pygame.draw.rect(screen, green, (x, y, 120, 180), 0)
        #desenha botão exit
        pygame.draw.rect(screen, yellow, (50,650,140,30), 2)
        my_font.render_to(screen, (100,655), "Exit", yellow)
        #desenha o score
        my_font.render_to(screen, (50,50), "Score: " + str(score), yellow)
        #muda as cores de amarelo para branco
        pos = pygame.mouse.get_pos()
        if(420<pos[0]<420+120 and 60<pos[1]<60+180):
            pygame.draw.rect(screen, white, (420,60,120,180), 0)
        else:
            pygame.draw.rect(screen, green, (420,60,120,180), 0)
        
        if(580<pos[0]<580+120 and 60<pos[1]<60+180):
            pygame.draw.rect(screen, white, (580,60,120,180), 0)
        else:
            pygame.draw.rect(screen, green, (580,60,120,180), 0)
        
        if(740<pos[0]<740+120 and 60<pos[1]<60+180):
            pygame.draw.rect(screen, white, (740,60,120,180), 0)
        else:
            pygame.draw.rect(screen, green, (740,60,120,180), 0)
        
        if(900<pos[0]<900+120 and 60<pos[1]<60+180):
            pygame.draw.rect(screen, white, (900,60,120,180), 0)
        else:
            pygame.draw.rect(screen, green, (900,60,120,180), 0)
        
        if(420<pos[0]<420+120 and 280<pos[1]<280+180):
            pygame.draw.rect(screen, white, (420,280,120,180), 0)
        else:
            pygame.draw.rect(screen, green, (420,280,120,180), 0)
        
        if(580<pos[0]<580+120 and 280<pos[1]<280+180):
            pygame.draw.rect(screen, white, (580,280,120,180), 0)
        else:
            pygame.draw.rect(screen, green, (580,280,120,180), 0)
        
        if(740<pos[0]<740+120 and 280<pos[1]<280+180):
            pygame.draw.rect(screen, white, (740,280,120,180), 0)
        else:
            pygame.draw.rect(screen, green, (740,280,120,180), 0)
        
        if(900<pos[0]<900+120 and 280<pos[1]<280+180):
            pygame.draw.rect(screen, white, (900,280,120,180), 0)
        else:
            pygame.draw.rect(screen, green, (900,280,120,180), 0)
        
        if(420<pos[0]<420+120 and 500<pos[1]<500+180):
            pygame.draw.rect(screen, white, (420,500,120,180), 0)
        else:
            pygame.draw.rect(screen, green, (420,500,120,180), 0)
        
        if(580<pos[0]<580+120 and 500<pos[1]<500+180):
            pygame.draw.rect(screen, white, (580,500,120,180), 0)
        else:
            pygame.draw.rect(screen, green, (580,500,120,180), 0)
        
        if(740<pos[0]<740+120 and 500<pos[1]<500+180):
            pygame.draw.rect(screen, white, (740,500,120,180), 0)
        else:
            pygame.draw.rect(screen, green, (740,500,120,180), 0)
        
        if(900<pos[0]<900+120 and 500<pos[1]<500+180):
            pygame.draw.rect(screen, white, (900,500,120,180), 0)
        else:
            pygame.draw.rect(screen, green, (900,500,120,180), 0)
        
        if(50<pos[0]<50+140 and 650<pos[1]<650+30):
            pygame.draw.rect(screen, white, (50,650,140,30), 2)
            my_font.render_to(screen, (100,655), "Exit", white)
        
        pygame.display.flip()
        click = pygame.mouse.get_pressed()
        #voltar ao menu
        if(50<pos[0]<50+140 and 650<pos[1]<650+30 and click[0]):
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
        click = pygame.mouse.get_pressed()
        #voltar ao menu
        if(50<pos[0]<50+140 and 650<pos[1]<650+30 and click[0]):
            main()

def main():
    while(True):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                exit()
        screen.fill((0,0,20))
        #desenha o menu
        pygame.draw.rect(screen, yellow, (650,370-40,140,30), 2)
        pygame.draw.rect(screen, yellow, (650,370,140,30), 2)
        pygame.draw.rect(screen, yellow, (650,370+40,140,30), 2)
        pygame.draw.rect(screen, yellow, (650,370+80,140,30), 2)
        pygame.draw.rect(screen, yellow, (650,370+120,140,30), 2)
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
        click = pygame.mouse.get_pressed()
        if(650<pos[0]<650+140 and 370+180<pos[1]<370+180+30 and click[0]):
            exit()
        #Nivel 1
        if(650<pos[0]<650+140 and 370-40<pos[1]<370-40+30 and click[0]):
            lvl1()
        
        if(650<pos[0]<650+140 and 370<pos[1]<370+30 and click[0]):
            lvl2()
main()
