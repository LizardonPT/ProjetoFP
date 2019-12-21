import pygame
import pygame.freetype
def main():
    pygame.init()
    res = (1440, 740)
    screen = pygame.display.set_mode(res)
    image = pygame.image.load("shuffle.png")
    my_font = pygame.freetype.Font("NotoSans-Regular.ttf", 24)

    while(True):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                exit()
        screen.fill((0,0,20))
        pygame.draw.rect(screen, (255,255,0), ((1440/2)-70,(740/2)-40,140,30), 2)
        pygame.draw.rect(screen, (255,255,0), ((1440/2)-70,740/2,140,30), 2)
        pygame.draw.rect(screen, (255,255,0), ((1440/2)-70,(740/2)+40,140,30), 2)
        pygame.draw.rect(screen, (255,255,0), ((1440/2)-70,(740/2)+80,140,30), 2)
        pygame.draw.rect(screen, (255,255,0), ((1440/2)-70,(740/2)+120,140,30), 2)
        pygame.draw.rect(screen, (255,255,0), ((1440/2)-70,(740/2)+180,140,30), 2)
        screen.blit(image, ((740/2)-35,0))
        my_font.render_to(screen, ((1440/2)-20,(740/2)-35), "4x3", (255,255,0))
        my_font.render_to(screen, ((1440/2)-20,(740/2)+5), "4x4", (255,255,0))
        my_font.render_to(screen, ((1440/2)-20,(740/2)+45), "4x5", (255,255,0))
        my_font.render_to(screen, ((1440/2)-20,(740/2)+85), "4x6", (255,255,0))
        my_font.render_to(screen, ((1440/2)-20,(740/2)+125), "4x7", (255,255,0))
        my_font.render_to(screen, ((1440/2)-20,(740/2)+185), "Exit", (255,255,0))
        pygame.display.flip()
main()
