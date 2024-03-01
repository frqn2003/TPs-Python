import pygame
import sys
import random

pygame.init()

blanco = (255, 255, 255)
negro = (0, 0, 0)
azul = (53, 79, 194)

pantalla_ancho = 800
pantalla_largo = 600

from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super(Jugador, self).__init__()
        self.surf = pygame.image.load("jet.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()
        self.rect.topleft = (pantalla_ancho / 2, pantalla_largo / 2)

    def update(self, teclas_presionadas):
        if teclas_presionadas[K_UP]:
            self.rect.move_ip(0, -1)
        if teclas_presionadas[K_DOWN]:
            self.rect.move_ip(0, 1)
        if teclas_presionadas[K_LEFT]:
            self.rect.move_ip(-1, 0)
        if teclas_presionadas[K_RIGHT]:
            self.rect.move_ip(1, 0)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > pantalla_ancho:
            self.rect.right = pantalla_ancho
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= pantalla_largo:
            self.rect.bottom = pantalla_largo

class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super(Cloud, self).__init__()
        self.surf = pygame.image.load("cloud.png").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(pantalla_ancho + 20, pantalla_ancho + 100),
                random.randint(0, pantalla_largo),
            )
        )

    def update(self):
        self.rect.move_ip(-1, 0)
        if self.rect.right < 0:
            self.kill()

ADDCLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADDCLOUD, 1000)

pantalla = pygame.display.set_mode([pantalla_ancho, pantalla_largo])
pygame.display.set_caption("Proyecto")

jugador = Jugador()
clouds = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

condicion = True
while condicion:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            condicion = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                condicion = False
        elif event.type == ADDCLOUD:
            new_cloud = Cloud()
            clouds.add(new_cloud)
            all_sprites.add(new_cloud)

    teclas_presionadas = pygame.key.get_pressed()
    jugador.update(teclas_presionadas)

    for cloud in clouds:
        if pygame.sprite.collide_rect(jugador, cloud):
            # Realiza alguna acción cuando el jugador colisiona con una nube
            pass

    all_sprites.update()
    
    pantalla.fill(azul)
    pantalla.blit(jugador.surf, jugador.rect.topleft)
    for entity in all_sprites:
        pantalla.blit(entity.surf, entity.rect)
    
    pygame.display.update()

pygame.quit()
sys.exit()
