import pygame, sys, random
pygame.init()
size=(800,600)
screen = pygame.display.set_mode(size)
#Manejo del reloj
clock=pygame.time.Clock()
game_over=False
BLACK=(0,0,0)
WHITE=(255,255,255)
font = pygame.font.SysFont("terminal",50)
text1=font.render('0',True,WHITE,)
Textrect1=text1.get_rect()
Textrect1.center = 100,20
text2=font.render('1',True,WHITE,)
Textrect2=text1.get_rect()
Textrect2.center = 500,20
screen.blit(text2, Textrect2)

while not game_over:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            game_over=True
            sys.exit()
    screen.fill(BLACK)
    screen.blit(text1, Textrect1)
    screen.blit(text2, Textrect2)
        #Actualiza Pantalla
    pygame.display.flip()
    clock.tick(120)