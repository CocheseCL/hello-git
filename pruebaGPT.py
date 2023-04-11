import pygame, sys, random, math
pygame.init()

# Inicializar atributos básicos
size = (800, 600)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
game_over = False
p1_altura = 90
p1_ancho = 15
puntaje_p1 = 0
puntaje_p2 = 0
music=pygame.mixer.music.load('Sonidos/music.mp3')
plip=pygame.mixer.Sound('Sonidos/pop1.wav')
plop=pygame.mixer.Sound('Sonidos/pop2.wav')
punto=pygame.mixer.Sound('Sonidos/fart.wav')
pygame.mixer.music.play(-1)
# Definir colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

font = pygame.font.SysFont("terminal", 50)
text1 = font.render(str(puntaje_p1), True, WHITE)
Textrect1 = text1.get_rect()
Textrect1.center = size[0] / 3, size[1] / 30
text2 = font.render(str(puntaje_p2), True, WHITE)
Textrect2 = text1.get_rect()
Textrect2.center = (size[0] / 3) * 2, size[1] / 30
screen.blit(text2, Textrect2)

player1_x_coor = 30
player1_y_coor = 300 - 45
player1_y_speed = 0

player2_x_coor = 750
player2_y_coor = 300 - 45
player2_y_speed = 0

pelota_x = 400
pelota_y = 300
pelota_speed_x = 3
pelota_speed_y = 3 * random.randint(-10, 10) / 10

player1_limite_up = False
player2_limite_up = False
player1_limite_down = False
player2_limite_down = False

coor_estrella = []
for i in range(60):
    vel = random.randint(1, 3) / 4  # Velocidad Movimiento
    x = random.randint(0, 800)  # Posición eje X
    y = random.randint(0, 600)  # Posición eje Y
    coor_estrella.append([x, y, vel])

pygame.mouse.set_visible(0)


def create_powerup():
    posx = random.randint(100, size[0]-100)
    posy = size[1] - 30
    TipoPoder=['D','X','M']
    text = font.render(random.choice(TipoPoder), True, random.choice((WHITE,GREEN)))
    Textrect = text.get_rect()
    Textrect.center = posx + 20, posy + 15
    return {
        'posx': posx,
        'posy': posy,
        'text': text,
        'Textrect': Textrect,
        'angulo': 0.0001,
        'velocidad_x': random.choice((1,-1)),
    }
powerups = []

def process_input():
    global player1_y_speed, player2_y_speed

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            # Jugador 1
            if event.key == pygame.K_w:
                if not player1_limite_up:
                    player1_y_speed = -3
                else:
                    player1_y_speed = 0
            if event.key == pygame.K_s:
                if not player1_limite_down:
                    player1_y_speed = 3
                else:
                    player1_y_speed = 0
            # Jugador 2
            if event.key == pygame.K_UP:
                if not player2_limite_up:
                    player2_y_speed = -3
                else:
                    player2_y_speed = 0
            if event.key == pygame.K_DOWN:
                if not player2_limite_down:
                    player2_y_speed = 3
                else:
                    player2_y_speed = 0
            if event.key == pygame.K_SPACE:
                powerups.append(create_powerup())
        if event.type == pygame.KEYUP:
            # Jugador 1
            if event.key == pygame.K_w:
                player1_y_speed = 0
            if event.key == pygame.K_s:
                player1_y_speed = 0
            # Jugador 2
            if event.key == pygame.K_UP:
                player2_y_speed = 0
            if event.key == pygame.K_DOWN:
                player2_y_speed = 0

def update_positions():
    global pelota_x, pelota_y, player1_y_coor, player2_y_coor,pelota_speed_x,pelota_speed_y
    if pelota_y > 590 or pelota_y < 10:
        pelota_speed_y *= -1
    player1_y_coor += player1_y_speed
    player2_y_coor += player2_y_speed
    pelota_x += pelota_speed_x * 0.6
    pelota_y += pelota_speed_y * 0.6

def check_bounds():
    global player1_limite_up, player1_limite_down, player2_limite_up, player2_limite_down,player1_y_speed,player2_y_speed
    if player1_y_coor < 0:
        player1_y_speed = 0
        player1_limite_up = True
    else:
        player1_limite_up = False
    if player1_y_coor > 600 - p1_altura:
        player1_y_speed = 0
        player1_limite_down = True
    else:
        player1_limite_down = False
    if player2_y_coor < 0:
        player2_y_speed = 0
        player2_limite_up = True
    else:
        player2_limite_up = False
    if player2_y_coor > 600 - p1_altura:
        player2_y_speed = 0
        player2_limite_down = True
    else:
        player2_limite_down = False
def check_pelota_out():
    global pelota_x, pelota_y, pelota_speed_x, pelota_speed_y, puntaje_p1, puntaje_p2
    if pelota_x > 800:
        pelota_x = 400
        pelota_y = 300
        pelota_speed_x = 3 * random.choice((1, -1))
        pelota_speed_y = 3 * random.randint(-10, 10) / 11
        puntaje_p1 += 1
        punto.play()

    if pelota_x < 0:
        pelota_x = 400
        pelota_y = 300
        pelota_speed_x = 3 * random.choice((1, -1))
        pelota_speed_y = 3 * random.randint(-10, 10) / 11
        puntaje_p2 += 1
        punto.play()

def check_collisions():
    global pelota_speed_x, pelota_speed_y,player1_speed,player2_speed
    if pelota.colliderect(jugador1) or pelota.colliderect(jugador2):
        pelota_speed_x *= -1
        if pelota.colliderect(jugador1):
            paddle = jugador1
            velocidad = player1_y_speed
            plip.play();
        else:
            paddle = jugador2
            velocidad = player2_y_speed
            plop.play();

        offset = (pelota.centery - paddle.centery) / (p1_altura / 2) + velocidad / 5
        pelota_speed_y = offset * 5




def draw_stars():
    for i in range(len(coor_estrella)):
        x, y, vel = coor_estrella[i]
        pygame.draw.circle(screen, WHITE, (int(x), int(y)), 1)
        x += vel
        if x > size[0]:
            x = 0
            y = random.randint(0, 600)
        coor_estrella[i] = [x, y, vel]

def draw_score():
    text1 = font.render(str(puntaje_p1), True, WHITE)
    Textrect1.center = size[0] / 3, size[1] / 30
    text2 = font.render(str(puntaje_p2), True, WHITE)
    Textrect2.center = (size[0] / 3) * 2, size[1] / 30
    screen.blit(text1, Textrect1)
    screen.blit(text2, Textrect2)

while not game_over:
    process_input()
    update_positions()
    check_bounds()
    check_pelota_out()
    screen.fill(BLACK)
    draw_stars()
    jugador1 = pygame.draw.rect(screen, GREEN, (player1_x_coor, player1_y_coor, p1_ancho, p1_altura))
    jugador2 = pygame.draw.rect(screen, BLUE, (player2_x_coor, player2_y_coor, p1_ancho, p1_altura))
    pelota = pygame.draw.circle(screen, RED, (pelota_x, pelota_y), 10)
    check_collisions()
    for powerup in powerups:
        powerup_rect = pygame.Rect(powerup['posx'], powerup['posy'], 40, 30)
        if powerup_rect.colliderect(jugador1) or powerup_rect.colliderect(jugador2):
            powerups.remove(powerup)
        else:
            if powerup['posx'] > size[0] - 40:
                powerup['velocidad_x'] *= -1
            if powerup['posx'] < 0:
                powerup['velocidad_x'] *= -1

            powerup['posx'] += powerup['velocidad_x']
            powerup['posy'] -= math.sin(powerup['angulo']) * 1.430
            powerup['angulo'] += 0.005
            pygame.draw.rect(screen, WHITE, (powerup['posx'], powerup['posy'], 40, 30), 3, 2, 10, 10, 10, 10)
            powerup['Textrect'].center = powerup['posx'] + 20, powerup['posy'] + 15
            screen.blit(powerup['text'], powerup['Textrect'])
    draw_score()
    pygame.display.update()
    clock.tick(120)

