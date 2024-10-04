import pygame
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self, missile_image_path, scale_factor, screen_width, screen_height):
        super(Enemy, self).__init__()
        self.surf = pygame.image.load(missile_image_path).convert() 
        self.surf.set_colorkey((255, 255, 255)) 
        self.surf = pygame.transform.scale(self.surf, 
            (int(self.surf.get_width() * scale_factor), 
             int(self.surf.get_height() * scale_factor)))  # Escalar la imagen
        self.rect = self.surf.get_rect(
            center=(
                random.randint(screen_width + 20, screen_width + 100),
                random.randint(80, screen_height - 80),  
            )
        )
        self.speed = random.randint(30, 50)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
