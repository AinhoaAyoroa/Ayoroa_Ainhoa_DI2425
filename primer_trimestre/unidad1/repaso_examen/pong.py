import pygame
from pygame.locals import K_UP, K_DOWN, K_w, K_s, K_ESCAPE, KEYDOWN, QUIT

# COLORES
blanco = (255, 255, 255)
negro = (0, 0, 0)

# CLASE JUGADOR
class Player(pygame.sprite.Sprite):
    def __init__(self, start_pos):
        super().__init__()
        self.surf = pygame.Surface((25, 95))
        self.surf.fill(blanco)
        self.rect = self.surf.get_rect(topleft=start_pos)

    def update(self, pressed_keys, up_key, down_key):
        if pressed_keys[up_key]:
            self.rect.move_ip(0, -10)
        if pressed_keys[down_key]:
            self.rect.move_ip(0, 10)
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT - 20:
            self.rect.bottom = SCREEN_HEIGHT - 20

# CLASE BOLA
class Ball(pygame.sprite.Sprite):
    def __init__(self, start_pos):
        super().__init__()
        self.surf = pygame.Surface((30, 30))
        self.surf.fill(blanco)
        self.rect = self.surf.get_rect(topleft=start_pos)
        self.speed_X = 6
        self.speed_Y = 6

    def update(self):
        self.rect.move_ip(self.speed_X, self.speed_Y)
        if self.rect.bottom >= SCREEN_HEIGHT - 20 or self.rect.top <= 0:
            self.speed_Y *= -1

    def bounce(self):
        self.speed_X *= -1

pygame.init()
informacion_ventana = pygame.display.Info()
SCREEN_WIDTH, SCREEN_HEIGHT = informacion_ventana.current_w, informacion_ventana.current_h
ventana = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)

screen = ventana
clock = pygame.time.Clock()

player1 = Player((25, SCREEN_HEIGHT // 2 - 50))
player2 = Player((SCREEN_WIDTH - 50, SCREEN_HEIGHT // 2 - 50))
players = pygame.sprite.Group(player1, player2)

ball = Ball((SCREEN_WIDTH // 2 - 15, SCREEN_HEIGHT // 2 - 15))

running = True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            running = False
        elif event.type == QUIT:
            running = False

    pressed_keys = pygame.key.get_pressed()
    player1.update(pressed_keys, K_w, K_s)
    player2.update(pressed_keys, K_UP, K_DOWN)
    ball.update()

    if ball.rect.left <= 0 or ball.rect.right >= SCREEN_WIDTH:
        running = False

    screen.fill(negro)
    screen.blit(player1.surf, player1.rect)
    screen.blit(player2.surf, player2.rect)
    screen.blit(ball.surf, ball.rect)

    if pygame.sprite.spritecollideany(ball, players):
        ball.bounce()

    pygame.display.flip()
    clock.tick(120)

pygame.quit()
