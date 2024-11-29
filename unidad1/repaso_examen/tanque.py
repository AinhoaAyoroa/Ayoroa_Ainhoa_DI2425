import pygame
import math
from pygame.locals import K_UP, K_DOWN, K_LEFT, K_RIGHT, K_SPACE, K_ESCAPE, KEYDOWN, QUIT, K_a, K_d, K_w, K_s, K_RETURN

# COLORES
blanco = (255, 255, 255)
negro = (0, 0, 0)

# CLASE TANQUE
class Tank(pygame.sprite.Sprite):
    def __init__(self, start_pos, controls):
        super().__init__()
        self.surf = pygame.Surface((50, 50), pygame.SRCALPHA)
        self.surf.fill((0, 255, 0))
        self.rect = self.surf.get_rect(topleft=start_pos)
        self.angle = 0  # Dirección inicial
        self.controls = controls
        self.speed = 2
        self.rot_speed = 2  # Velocidad de rotación
    
    def update(self, pressed_keys):
        # Gira el tanque constantemente
        self.angle += self.rot_speed
        if self.angle >= 360:
            self.angle = 0
        
        # Movimiento del tanque solo si se presiona la tecla de avanzar
        if pressed_keys[self.controls['move']]:
            radian_angle = math.radians(self.angle)
            self.rect.x += math.cos(radian_angle) * self.speed
            self.rect.y -= math.sin(radian_angle) * self.speed
        
        # Disparar proyectil
        if pressed_keys[self.controls['shoot']]:
            return Bullet(self.rect.center, self.angle)  # Dispara un proyectil en la dirección en la que está mirando

        return None  # No se dispara nada si no se presiona la tecla de disparo
    
    def get_turret_pos(self):
        """ Devuelve la posición del 'cañón' para ver hacia donde apunta el tanque """
        radian_angle = math.radians(self.angle)
        return (self.rect.centerx + math.cos(radian_angle) * 25, 
                self.rect.centery - math.sin(radian_angle) * 25)

# CLASE PROYECTIL
class Bullet(pygame.sprite.Sprite):
    def __init__(self, start_pos, angle):
        super().__init__()
        self.surf = pygame.Surface((10, 10))
        self.surf.fill(blanco)
        self.rect = self.surf.get_rect(center=start_pos)
        self.angle = angle
        self.speed = 5

    def update(self):
        radian_angle = math.radians(self.angle)
        self.rect.x += math.cos(radian_angle) * self.speed
        self.rect.y -= math.sin(radian_angle) * self.speed

# CONFIGURACIÓN PYGAME
pygame.init()
informacion_ventana = pygame.display.Info()
SCREEN_WIDTH, SCREEN_HEIGHT = informacion_ventana.current_w, informacion_ventana.current_h
ventana = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)

screen = ventana
clock = pygame.time.Clock()

# CONTROL DE LAS TECLAS
controls_player1 = {'move': K_w, 'shoot': K_SPACE}
controls_player2 = {'move': K_UP, 'shoot': K_RETURN}

# CREACIÓN DE JUGADORES Y GRUPOS
player1 = Tank((100, SCREEN_HEIGHT // 2), controls_player1)
player2 = Tank((SCREEN_WIDTH - 150, SCREEN_HEIGHT // 2), controls_player2)
players = pygame.sprite.Group(player1, player2)

bullets = pygame.sprite.Group()

# BUCLE PRINCIPAL DEL JUEGO
running = True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            running = False
        elif event.type == QUIT:
            running = False

    pressed_keys = pygame.key.get_pressed()

    # Actualiza el estado de los tanques
    new_bullet1 = player1.update(pressed_keys)
    if new_bullet1:
        bullets.add(new_bullet1)

    new_bullet2 = player2.update(pressed_keys)
    if new_bullet2:
        bullets.add(new_bullet2)

    # Actualiza las balas
    for bullet in bullets:
        bullet.update()

    # Colisiones de balas con jugadores
    if new_bullet2 and pygame.sprite.collide_rect(player1, new_bullet2):
        print("¡Jugador 1 ha sido alcanzado! Fin del juego.")
        running = False

    if new_bullet1 and pygame.sprite.collide_rect(player2, new_bullet1):
        print("¡Jugador 2 ha sido alcanzado! Fin del juego.")
        running = False

    # Dibuja todo
    screen.fill(negro)

    # Dibuja tanques
    player1_rotated = pygame.transform.rotate(player1.surf, player1.angle)
    player1_rect = player1_rotated.get_rect(center=player1.rect.center)
    screen.blit(player1_rotated, player1_rect)

    player2_rotated = pygame.transform.rotate(player2.surf, player2.angle)
    player2_rect = player2_rotated.get_rect(center=player2.rect.center)
    screen.blit(player2_rotated, player2_rect)

    # Dibuja misiles
    for bullet in bullets:
        screen.blit(bullet.surf, bullet.rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
