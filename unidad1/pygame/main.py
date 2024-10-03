import os
import pygame
import random
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT
)

pygame.init()
pygame.mixer.init() 

# Obtener la ruta del directorio del archivo actual
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SOUND_DIR = os.path.join(BASE_DIR, "sound")  # Ruta a la carpeta de sonidos

# Cargar y reproducir música de fondo
pygame.mixer.music.load(os.path.join(SOUND_DIR, "Apoxode_-_Electric_1.ogg"))
pygame.mixer.music.play(loops=-1)

# Cargar todos los archivos de sonido
move_up_sound = pygame.mixer.Sound(os.path.join(SOUND_DIR, "Rising_putter.ogg"))
move_down_sound = pygame.mixer.Sound(os.path.join(SOUND_DIR, "Falling_putter.ogg"))
collision_sound = pygame.mixer.Sound(os.path.join(SOUND_DIR, "Collision.ogg"))  # Sonido de colisión

# Definir las rutas de las imágenes de forma relativa
JET_IMAGE_PATH = os.path.join(BASE_DIR, "resources", "jet.png")
CLOUD_IMAGE_PATH = os.path.join(BASE_DIR, "resources", "cloud.png")
MISSILE_IMAGE_PATH = os.path.join(BASE_DIR, "resources", "missile.png")  # Ruta para los misiles

info = pygame.display.Info()
SCREEN_WIDTH = info.current_w
SCREEN_HEIGHT = info.current_h

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)

clock = pygame.time.Clock()

# Factor de escala para aumentar el tamaño de las imágenes
SCALE_FACTOR = 2.5

# Definir un objeto Jugador extendiendo pygame.sprite.Sprite
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load(JET_IMAGE_PATH).convert()
        self.surf.set_colorkey((255, 255, 255))  # Establece el color clave para el jet
        self.surf = pygame.transform.scale(self.surf, (int(self.surf.get_width() * SCALE_FACTOR), int(self.surf.get_height() * SCALE_FACTOR)))  # Escalar la imagen
        self.rect = self.surf.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))

    # Función para actualizar la posición del jugador
    def update(self, pressed_keys):
        # Aumentar velocidad de movimiento del jugador a 20
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -20)  
            move_up_sound.play()  
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 20)
            move_down_sound.play()
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-20, 0)  
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(20, 0)

        # Mantener al jugador dentro de los límites de la pantalla con un margen
        MARGIN = 74
        if self.rect.left < MARGIN:
            self.rect.left = MARGIN
        if self.rect.right > SCREEN_WIDTH - MARGIN:  
            self.rect.right = SCREEN_WIDTH - MARGIN
        if self.rect.top < MARGIN:
            self.rect.top = MARGIN
        if self.rect.bottom > SCREEN_HEIGHT - MARGIN:  
            self.rect.bottom = SCREEN_HEIGHT - MARGIN

class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super(Cloud, self).__init__()
        self.surf = pygame.image.load(CLOUD_IMAGE_PATH).convert_alpha() 
        self.surf = pygame.transform.scale(self.surf, (int(self.surf.get_width() * SCALE_FACTOR), int(self.surf.get_height() * SCALE_FACTOR)))  # Escalar la imagen de la nube
        self.rect = self.surf.get_rect(
            center=(
                SCREEN_WIDTH + 20,
                random.randint(50, SCREEN_HEIGHT - 50)
            )
        )

    def update(self):
        self.rect.move_ip(-40, 0)
        if self.rect.right < 0:
            self.kill()

# Definir el objeto enemigo extendiendo pygame.sprite.Sprite
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.image.load(MISSILE_IMAGE_PATH).convert() 
        self.surf.set_colorkey((255, 255, 255)) 
        self.surf = pygame.transform.scale(self.surf, (int(self.surf.get_width() * SCALE_FACTOR), int(self.surf.get_height() * SCALE_FACTOR)))  # Escalar la imagen
        # Ampliar rango para que aparezcan más dispersos en el eje y
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(80, SCREEN_HEIGHT - 80),  # Aparecerán más dispersos
            )
        )
        self.speed = random.randint(30, 50)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()


ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 500)  

# Crear un evento para agregar nubes
ADDCLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADDCLOUD, 1000)  

player = Player()

enemies = pygame.sprite.Group()
clouds = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

running = True

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
        elif event.type == ADDENEMY:
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)
        elif event.type == ADDCLOUD:
            new_cloud = Cloud()
            clouds.add(new_cloud)
            all_sprites.add(new_cloud)

    pressed_keys = pygame.key.get_pressed()

    player.update(pressed_keys)
    enemies.update()
    clouds.update()

    # azul claro
    screen.fill((135, 206, 250))

    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    # Comprobar colisiones entre el jugador y los enemigos
    if pygame.sprite.spritecollideany(player, enemies):
        collision_sound.play()  
        player.kill()
        running = False

    pygame.display.flip()
    clock.tick(30)

pygame.mixer.music.stop()  
pygame.mixer.quit()
pygame.quit() 
