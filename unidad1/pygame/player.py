import os
import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT
)

class Player(pygame.sprite.Sprite):
    def __init__(self, jet_image_path, scale_factor, screen_width, screen_height):
        super(Player, self).__init__()
        self.surf = pygame.image.load(jet_image_path).convert()
        self.surf.set_colorkey((255, 255, 255))  # Establece el color clave para el jet
        self.surf = pygame.transform.scale(self.surf, 
            (int(self.surf.get_width() * scale_factor), 
             int(self.surf.get_height() * scale_factor)))  # Escalar la imagen
        self.rect = self.surf.get_rect(center=(screen_width / 2, screen_height / 2))
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.move_up_sound = None
        self.move_down_sound = None

    def set_sounds(self, move_up_sound, move_down_sound):
        self.move_up_sound = move_up_sound
        self.move_down_sound = move_down_sound

    def update(self, pressed_keys):
        # Aumentar velocidad de movimiento del jugador a 20
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -20)  
            self.move_up_sound.play()  
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 20)
            self.move_down_sound.play()
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-20, 0)  
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(20, 0)

        # Mantener al jugador dentro de los límites de la pantalla con un margen
        MARGIN = 74
        if self.rect.left < MARGIN:
            self.rect.left = MARGIN
        if self.rect.right > self.screen_width - MARGIN:  
            self.rect.right = self.screen_width - MARGIN
        if self.rect.top < MARGIN:
            self.rect.top = MARGIN
        if self.rect.bottom > self.screen_height - MARGIN:  
            self.rect.bottom = self.screen_height - MARGIN
