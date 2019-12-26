import pygame
import pygame.freetype

def main():
    pygame.init()
    res = (1440, 740)
    screen = pygame.display.set_mode(res)
    image = pygame.image.load("shuffle.png")
    my_font = pygame.freetype.Font("NotoSans-Regular.ttf", 24)
    yellow = (255,255,0)
    white = (255,255,255)

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
        #def lvl1():
            #screen.fill(0,20,20)

        #if(650<pos[0]<650+140 and 370-40<pos[1]<370-40+30 and click[0]):
            #lvl1()
main()
