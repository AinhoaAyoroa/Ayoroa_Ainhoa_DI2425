import os
import pygame
from player import Player
from enemy import Enemy
from cloud import Cloud
from pygame.locals import (
    KEYDOWN,
    K_ESCAPE,
    QUIT
)

class Main:
    def __init__(self):
        pygame.init()
        pygame.mixer.init() 

        # Obtener la ruta del directorio del archivo actual
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        SOUND_DIR = os.path.join(BASE_DIR, "sound")

        # Cargar y reproducir música de fondo
        pygame.mixer.music.load(os.path.join(SOUND_DIR, "Apoxode_-_Electric_1.ogg"))
        pygame.mixer.music.play(loops=-1)

        # Cargar sonidos
        self.move_up_sound = pygame.mixer.Sound(os.path.join(SOUND_DIR, "Rising_putter.ogg"))
        self.move_down_sound = pygame.mixer.Sound(os.path.join(SOUND_DIR, "Falling_putter.ogg"))
        self.collision_sound = pygame.mixer.Sound(os.path.join(SOUND_DIR, "Collision.ogg"))

        # Definir las rutas de las imágenes como atributos de clase
        self.JET_IMAGE_PATH = os.path.join(BASE_DIR, "resources", "jet.png")
        self.CLOUD_IMAGE_PATH = os.path.join(BASE_DIR, "resources", "cloud.png")
        self.MISSILE_IMAGE_PATH = os.path.join(BASE_DIR, "resources", "missile.png")

        # Obtener dimensiones de la pantalla
        info = pygame.display.Info()
        self.SCREEN_WIDTH = info.current_w
        self.SCREEN_HEIGHT = info.current_h
        self.SCALE_FACTOR = 2.5

        # Inicializar la pantalla
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT), pygame.FULLSCREEN)

        self.clock = pygame.time.Clock()

        # Inicializar el jugador
        self.player = Player(self.JET_IMAGE_PATH, self.SCALE_FACTOR, self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        self.player.set_sounds(self.move_up_sound, self.move_down_sound)

        # Grupos de sprites
        self.enemies = pygame.sprite.Group()
        self.clouds = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player)

        # Eventos personalizados
        self.ADDENEMY = pygame.USEREVENT + 1
        pygame.time.set_timer(self.ADDENEMY, 500)  

        self.ADDCLOUD = pygame.USEREVENT + 2
        pygame.time.set_timer(self.ADDCLOUD, 1000)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN and event.key == K_ESCAPE:
                    running = False
                elif event.type == QUIT:
                    running = False
                elif event.type == self.ADDENEMY:
                    # Crear enemigo usando el atributo de clase MISSILE_IMAGE_PATH
                    new_enemy = Enemy(self.MISSILE_IMAGE_PATH, self.SCALE_FACTOR, self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
                    self.enemies.add(new_enemy)
                    self.all_sprites.add(new_enemy)
                elif event.type == self.ADDCLOUD:
                    # Crear nube usando el atributo de clase CLOUD_IMAGE_PATH
                    new_cloud = Cloud(self.CLOUD_IMAGE_PATH, self.SCALE_FACTOR, self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
                    self.clouds.add(new_cloud)
                    self.all_sprites.add(new_cloud)

            pressed_keys = pygame.key.get_pressed()

            # Actualizar entidades
            self.player.update(pressed_keys)
            self.enemies.update()
            self.clouds.update()

            # Azul claro de fondo
            self.screen.fill((135, 206, 250))

            # Dibujar todas las entidades
            for entity in self.all_sprites:
                self.screen.blit(entity.surf, entity.rect)

            # Comprobar colisiones
            if pygame.sprite.spritecollideany(self.player, self.enemies):
                self.collision_sound.play()  
                self.player.kill()
                running = False

            pygame.display.flip()
            self.clock.tick(30)

        pygame.mixer.music.stop()  
        pygame.mixer.quit()
        pygame.quit()

if __name__ == "__main__":
    game = Main()
    game.run()
