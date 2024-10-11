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

        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        SOUND_DIR = os.path.join(BASE_DIR, "sound")

        self.level = 1
        self.enemy_spawn_time = 1000

        pygame.mixer.music.load(os.path.join(SOUND_DIR, "Apoxode_-_Electric_1.ogg"))
        pygame.mixer.music.play(loops=-1)

        self.move_up_sound = pygame.mixer.Sound(os.path.join(SOUND_DIR, "Rising_putter.ogg"))
        self.move_down_sound = pygame.mixer.Sound(os.path.join(SOUND_DIR, "Falling_putter.ogg"))
        self.collision_sound = pygame.mixer.Sound(os.path.join(SOUND_DIR, "Collision.ogg"))

        self.JET_IMAGE_PATH = os.path.join(BASE_DIR, "resources", "jet.png")
        self.CLOUD_IMAGE_PATH = os.path.join(BASE_DIR, "resources", "cloud.png")
        self.MISSILE_IMAGE_PATH = os.path.join(BASE_DIR, "resources", "missile.png")
        self.NIGHT_IMAGE_PATH = os.path.join(BASE_DIR, "resources", "night.png")

        info = pygame.display.Info()
        self.SCREEN_WIDTH = info.current_w
        self.SCREEN_HEIGHT = info.current_h
        self.SCALE_FACTOR = 2

        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))

        self.clock = pygame.time.Clock()

        self.player = Player(self.JET_IMAGE_PATH, self.SCALE_FACTOR, self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        self.player.set_sounds(self.move_up_sound, self.move_down_sound)
        self.enemies = pygame.sprite.Group()
        self.clouds = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player)

        self.ADDENEMY = pygame.USEREVENT + 1
        pygame.time.set_timer(self.ADDENEMY, self.enemy_spawn_time)
        self.ADDCLOUD = pygame.USEREVENT + 2
        pygame.time.set_timer(self.ADDCLOUD, 1000)

        self.day_night_cycle = 20000
        self.time_elapsed = 0
        self.day = True

        self.max_score = 0
        if os.path.exists('punt_max.txt'):
            with open('punt_max.txt', 'r') as file:
                self.max_score = int(file.read().strip())

        self.night_background = pygame.image.load(self.NIGHT_IMAGE_PATH).convert() 
        self.night_background = pygame.transform.scale(self.night_background, (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))  

    def run(self):
        running = True
        score = 0
        while running:
            self.time_elapsed += self.clock.get_time()

            if self.time_elapsed >= self.day_night_cycle:
                self.day = not self.day
                self.time_elapsed = 0

            for event in pygame.event.get():
                if event.type == KEYDOWN and event.key == K_ESCAPE:
                    running = False
                elif event.type == QUIT:
                    running = False
                elif event.type == self.ADDENEMY:
                    new_enemy = Enemy(self.MISSILE_IMAGE_PATH, self.SCALE_FACTOR, self.SCREEN_WIDTH, self.SCREEN_HEIGHT, self.level)
                    self.enemies.add(new_enemy)
                    self.all_sprites.add(new_enemy)
                elif event.type == self.ADDCLOUD:
                    new_cloud = Cloud(self.CLOUD_IMAGE_PATH, self.SCALE_FACTOR, self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
                    self.clouds.add(new_cloud)
                    self.all_sprites.add(new_cloud)

            pressed_keys = pygame.key.get_pressed()
            self.player.update(pressed_keys)
            self.enemies.update()
            self.clouds.update()

            if self.day:
                self.screen.fill((135, 206, 250))
            else:
                self.screen.blit(self.night_background, (0, 0))  

            score += 0.5
            tablero_score = pygame.font.Font(None, 35)
            img_puntos = tablero_score.render(f'Puntuación: {int(score)}', True, (255, 255, 255))
            marco_puntos = img_puntos.get_rect()
            marco_puntos.left = self.SCREEN_WIDTH - 220
            marco_puntos.top = 10

            level_display = tablero_score.render(f'Nivel: {self.level}', True, (255, 255, 255))
            marco_nivel = level_display.get_rect()
            marco_nivel.left = 10
            marco_nivel.top = 10

            for entity in self.all_sprites:
                self.screen.blit(entity.surf, entity.rect)

            if pygame.sprite.spritecollideany(self.player, self.enemies):
                self.collision_sound.play()
                self.player.kill()
                running = False

            self.screen.blit(img_puntos, marco_puntos)
            self.screen.blit(level_display, marco_nivel)
            pygame.display.flip()
            self.clock.tick(30)

            if score >= 500 * self.level:
                self.level += 1
                self.enemy_spawn_time = max(500 - self.level * 50, 100)
                pygame.time.set_timer(self.ADDENEMY, self.enemy_spawn_time)

        if score > self.max_score:
            with open('punt_max.txt', 'w') as file:
                file.write(str(int(score))) 
                self.max_score = score

        pygame.mixer.music.stop()  
        pygame.mixer.quit()
        pygame.quit()

if __name__ == "__main__":
    game = Main()
    game.run()
