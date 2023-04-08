import pygame, sys, random
pygame.init()

#Crear atributos básicos
#Tamaño Pantalla
size=(800,600)
screen = pygame.display.set_mode(size)
#Manejo del reloj
clock=pygame.time.Clock()
#Inicializa variables
game_over=False

p1_altura=90
p1_ancho=15


#Coordenadas y velocidad del jugador 1
player1_x_coor=30
player1_y_coor=300 - 45
player1_y_speed = 0

#Coordenadas y velocidad del jugador 1
player2_x_coor= 750
player2_y_coor= 300 - 45
player2_y_speed = 0

#Coordenadas de la pelota
pelota_x=400
pelota_y=300
pelota_speed_x=3
pelota_speed_y=3


# Definir colores
BLACK=(0,0,0)
WHITE=(255,255,255)
GREEN=(0,255,0)
RED=(255,0,0)
BLUE=(0,0,255)

#Genera estrellas en posición inicial aleatoria
coor_estrella=[]
for i in range(60):
        vel=random.randint(1,3) #Velocidad Movimiento
        x = random.randint(0,800) #Posición eje X
        y = random.randint(0,600) #Posición eje Y
        coor_estrella.append([x,y,vel])
        

#Ocultamos el cursor del mouse
pygame.mouse.set_visible(0)


while not game_over:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            game_over=True
            sys.exit()
        if event.type==pygame.KEYDOWN:
             #Jugador 1
             if event.key==pygame.K_w:
                  player1_y_speed=-3
             if event.key==pygame.K_s:
                  player1_y_speed=3
             #Jugador 2
             if event.key==pygame.K_UP:
                  player2_y_speed=-3
             if event.key==pygame.K_DOWN:
                  player2_y_speed=3
        if event.type==pygame.KEYUP:
             #Jugador 1
             if event.key==pygame.K_w:
                  player1_y_speed=0
             if event.key==pygame.K_s:
                  player1_y_speed=0
             #Jugador 2
             if event.key==pygame.K_UP:
                  player2_y_speed=0
             if event.key==pygame.K_DOWN:
                  player2_y_speed=0
    if pelota_y > 590 or pelota_y<10:
        pelota_speed_y *= -1
    # Modifica coordenadas jugadores
    player1_y_coor += player1_y_speed
    player2_y_coor += player2_y_speed

    #Movimiento Pelota
    pelota_x += pelota_speed_x*0.6
    pelota_y += pelota_speed_y*0.6
    
    #Revisa si la pelota sale del lado derecho
    if pelota_x>800:
         pelota_x=400
         pelota_y=300
         #Si sale de la pantalla, invierte dirección
         pelota_speed_x *=-1
         pelota_speed_y *=-1
     #Revisa si la pelota sale del lado izquierdo
    if pelota_x<0:
         pelota_x=400
         pelota_y=300
         #Si sale de la pantalla, invierte dirección
         pelota_speed_x *=-1
         pelota_speed_y *=-1

   
    screen.fill(BLACK)

    ### ---LOGICA DE JUEGO

    
 #DIBUJA ESTRELLAS
    for coord in coor_estrella:
        x=coord[0]
        y=coord[1]
        pygame.draw.circle(screen,WHITE,(x,y),2)
        coord[1] +=coord[2]/2
        if (coord[1] > 600):
            coord[1] = 0
            coord[0] = random.randint(0,800) 
   #Dibuja objetos
    jugador1=pygame.draw.rect(screen,GREEN,(player1_x_coor,player1_y_coor,p1_ancho,p1_altura))
    jugador2=pygame.draw.rect(screen,BLUE,(player2_x_coor,player2_y_coor,p1_ancho,p1_altura))
    pelota=pygame.draw.circle(screen,RED,(pelota_x,pelota_y),10)
    
    ###Lógica para no escapar (arreglar)
    if player1_y_coor==0 or player1_y_coor==600-p1_altura:
        player1_y_speed=0
    if player2_y_coor==0 or player2_y_coor==600-p1_altura:
        player2_y_speed=0
    #Colisiones
    if pelota.colliderect(jugador1) or pelota.colliderect(jugador2):
         pelota_speed_x*=-1
         
    
    #Actualiza Pantalla
    pygame.display.flip()
    clock.tick(120)