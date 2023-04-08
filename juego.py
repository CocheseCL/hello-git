import pygame, sys, random
pygame.init()
# Definir colores
BLACK=(0,0,0)
WHITE=(255,255,255)
GREEN=(0,255,0)
RED=(255,0,0)
BLUE=(0,0,255)

#Crear atributos básicos
size=(800,500)
screen = pygame.display.set_mode(size)
clock=pygame.time.Clock()
game_over=False



cord_x=400
cord_y=200
nuevo_x=10
nuevo_y=10
x_speed=0
y_speed=0

coor_list=[]
for i in range(60):
        vel=random.randint(1,3)
        x = random.randint(0,800) 
        y = random.randint(0,500)
        coor_list.append([x,y,vel])


#Velocidad Movimiento
speed_x=3
speed_y=2
pygame.mouse.set_visible(0)
while not game_over:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            game_over=True
            sys.exit()
        if event.type ==pygame.KEYDOWN:
             if event.key==pygame.K_LEFT:
                x_speed=-3
             if event.key==pygame.K_RIGHT:
                x_speed=3
             if event.key==pygame.K_UP:
                y_speed=-3
             if event.key==pygame.K_DOWN:
                y_speed=3
                  

        if event.type ==pygame.KEYUP:
             if event.key==pygame.K_LEFT:
                x_speed=0
             if event.key==pygame.K_RIGHT:
                x_speed=0
             if event.key==pygame.K_UP:
                y_speed=0
             if event.key==pygame.K_DOWN:
                y_speed=0
    mouse_pos= pygame.mouse.get_pos()
   # print(mouse_pos)
    screen.fill(BLACK)
    nuevo_x+=x_speed
    nuevo_y+=y_speed

    ### ---LOGICA DE JUEGO
    if (cord_x>720 or cord_x<0):
        speed_x *=-1
    if (cord_y>420 or cord_y<0):
        speed_y *=-1       
    
 #DIBUJA ESTRELLAS
    for coord in coor_list:
        x=coord[0]
        y=coord[1]
        pygame.draw.circle(screen,WHITE,(x,y),2)
        coord[1] +=coord[2]/2
        if (coord[1] > 500):
            coord[1] = 0
            coord[0] = random.randint(0,800) 
   #Dibuja objetos
    pygame.draw.rect(screen,GREEN, (nuevo_x,nuevo_y,40,40))
    pygame.draw.rect(screen,RED, (cord_x,cord_y,80,80))

    cord_x = mouse_pos[0]
    cord_y = mouse_pos[1]
    ###
    #Actualiza Pantalla
    pygame.display.flip()
    clock.tick(120)