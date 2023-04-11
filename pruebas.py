import pygame, sys, random,math

pygame.init()
size=(800,600)
screen = pygame.display.set_mode(size)
#Manejo del reloj
clock=pygame.time.Clock()
game_over=False
BLACK=(0,0,0)
WHITE=(255,255,255)
posx=random.randint(0,800)
posy=size[1]-30
velocidad_x=2
angulo=0.001
#print(pygame.font.get_fonts())
font = pygame.font.SysFont("terminal",30)
text1=font.render('D',True,WHITE)
Textrect1=text1.get_rect()
Textrect1.center = posx+20,posy+15


while not game_over:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            game_over=True
            sys.exit()
        if event.type ==pygame.KEYDOWN:
            pass
            #Crear PowerUp

    screen.fill(BLACK)

    #MOVER
    if posx>size[0]-30:
        velocidad_x *=-1
    if posx<0:
        velocidad_x *=-1

    posx=posx+velocidad_x
    posy=posy-math.sin(angulo)*1.430
    angulo += 0.005
    
    #print ("Posy="+str(posy))
    #print ("Seno="+str(math.sin(angulo)))

    
    pygame.draw.rect(screen,WHITE,(posx,posy,40,30),3,2,10,10,10,10)
    Textrect1=text1.get_rect()
    Textrect1.center = posx+20,posy+15
    screen.blit(text1, Textrect1)

        #Actualiza Pantalla
    pygame.display.flip()
    clock.tick(120)