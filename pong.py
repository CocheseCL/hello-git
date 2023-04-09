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
puntaje_p1=0
puntaje_p2=0

# Definir colores
BLACK=(0,0,0)
WHITE=(255,255,255)
GREEN=(0,255,0)
RED=(255,0,0)
BLUE=(0,0,255)

font = pygame.font.SysFont("terminal",50)
text1=font.render(str(puntaje_p1),True,WHITE)
Textrect1=text1.get_rect()
Textrect1.center = size[0]/3,size[1]/30
text2=font.render(str(puntaje_p2),True,WHITE)
Textrect2=text1.get_rect()
Textrect2.center = (size[0]/3)*2,size[1]/30
screen.blit(text2, Textrect2)

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
pelota_speed_y= 3 *  random.randint(-10,10)/10

#Limites
player1_limite_up=False
player2_limite_up=False
player1_limite_down=False
player2_limite_down=False



#Genera estrellas en posición inicial aleatoria
coor_estrella=[]
for i in range(60):
        vel=random.randint(1,3)/4 #Velocidad Movimiento
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
                  if player1_limite_up==False:
                       player1_y_speed=-3
                  else:
                       player1_y_speed=0
             if event.key==pygame.K_s:
                  if player1_limite_down==False:
                       player1_y_speed=3
                  else:
                       player1_y_speed=0
             #Jugador 2
             if event.key==pygame.K_UP:
                  if player2_limite_up==False:
                       player2_y_speed=-3
                  else:
                       player2_y_speed=0
             if event.key==pygame.K_DOWN:
                  if player2_limite_down==False:
                       player2_y_speed=3
                  else:
                       player2_y_speed=0
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
         #Si sale de la pantalla, Reinicia y aumenta puntaje
         pelota_speed_x = 3 * random.choice((1, -1))
         pelota_speed_y = 3 * random.randint(-10,10)/11
         puntaje_p1+=1
        
     #Revisa si la pelota sale del lado izquierdo
    if pelota_x<0:
         pelota_x=400
         pelota_y=300
         #Si sale de la pantalla,  Reinicia y aumenta puntaje
         pelota_speed_x = 3 * random.choice((1, -1))
         pelota_speed_y = 3 *  random.randint(-10,10)/11
         puntaje_p2+=1
         
   
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
    
    #Dibuja Puntaje
    text1=font.render(str(puntaje_p1),True,WHITE)
    text2=font.render(str(puntaje_p2),True,WHITE)
    screen.blit(text1, Textrect1)
    screen.blit(text2, Textrect2)
    ###Lógica para que los paddle no escapen
    if player1_y_coor<0:
        player1_y_speed=0
        player1_limite_up=True
    else:
        player1_limite_up=False
    if player1_y_coor>600-p1_altura:
        player1_y_speed=0
        player1_limite_down=True 
    else:
        player1_limite_down=False
    if player2_y_coor<0:
        player2_y_speed=0
        player2_limite_up=True
    else:
        player2_limite_up=False
    if player2_y_coor>600-p1_altura:
        player2_y_speed=0
        player2_limite_down=True 
    else:
        player2_limite_down=False

    #Colisiones
    if pelota.colliderect(jugador1) or pelota.colliderect(jugador2):
         pelota_speed_x*=-1
         if pelota.colliderect(jugador1):
          paddle = jugador1
          velocidad=player1_y_speed
         else:
          paddle = jugador2
          velocidad=player2_y_speed
         offset = (paddle.centery - pelota.centery) / (p1_altura / 2) + velocidad*-1/5
         pelota_speed_y = -offset * 5
         
   # print(pygame.time.get_ticks());
    #Actualiza Pantalla
    pygame.display.update()
    clock.tick(120)