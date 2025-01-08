import pygame

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
# C O L O R E S 
NEGRO = (0,0,0)
AZUL = (0, 0, 255)
BLANCO = (255, 255, 255)
# V E N T A N A
informacion_ventana = pygame.display.Info()
ancho = informacion_ventana.current_w
alto = informacion_ventana.current_h
ventana = pygame.display.set_mode((ancho, alto))
# B A C K G R O U N D
background_dia = AZUL
background_noche = NEGRO

en_marcha = True

while en_marcha:
    # bucle que controla todos los eventos del juego
    for event in pygame.event.get():    
       # el usuario ha apretado una tecla?
        if event.type == KEYDOWN:
          # el usuario ha apretado la tecla Esc?
            if event.key == K_ESCAPE:
                en_marcha = False
        elif event.type == QUIT:
            en_marcha = False


    ventana.fill(BLANCO)

    superficie = pygame.Surface((50, 50))
    superficie.fill((0,0,0))
    centro_superficie = (
        ( alto-superficie / 2 )
        ( ancho-superficie / 2 )
    )
    rect = superficie.get_rect()

    ventana.blit( superficie, centro_superficie )

    pygame.display.flip()
    
pygame.quit()