import pygame
import random

class Cloud(pygame.sprite.Sprite):
    def __init__(self, cloud_image_path, scale_factor, screen_width, screen_height):
        super(Cloud, self).__init__()
        self.surf = pygame.image.load(cloud_image_path).convert_alpha() 
        self.surf = pygame.transform.scale(self.surf, 
            (int(self.surf.get_width() * scale_factor), 
             int(self.surf.get_height() * scale_factor))) 
        self.rect = self.surf.get_rect(
            center=(
                screen_width + 20,
                random.randint(50, screen_height - 50)
            )
        )
        self.speed = 40  # Definir la velocidad de las nubes

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
