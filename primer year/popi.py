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
    K_ESCAPE,                                       ####TECLAS DEL JUEGO####
    K_SPACE,
    KEYDOWN,
    QUIT,
)
class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super(Jugador, self).__init__()
        self.superf = pygame.Surface((50, 50))
        self.surf = pygame.image.load("jet.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.superf.fill(azul)
        self.rect = self.superf.get_rect()
        self.rect.topleft = (pantalla_ancho/2, pantalla_largo/2)  # Coloca el jugador en el centro
    #Funcion para mover el personaje
    def update(self, teclas_presionadas):
        if teclas_presionadas[K_UP]:
            self.rect.move_ip(0, -1)        #Por ahora para cambiar la velocidad cambiar los valores que no sean 0
        if teclas_presionadas[K_DOWN]:
            self.rect.move_ip(0, 1)
        if teclas_presionadas[K_LEFT]:
            self.rect.move_ip(-1, 0)
        if teclas_presionadas[K_RIGHT]:
            self.rect.move_ip(1, 0)
        #Para que no se mueva afuera de la pantalla    
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
        super(Cloud, self)._init_()
        self.surf = pygame.image.load("cloud.png").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        # The starting position is randomly generated
        self.rect = self.surf.get_rect(
            center=(
                random.randint(pantalla_ancho + 20, pantalla_ancho + 100),
                random.randint(0, pantalla_largo),
            )
        )
ADDCLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADDCLOUD, 1000)
clouds = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
    # Move the cloud based on a constant speed
    # Remove the cloud when it passes the left edge of the screen
def update(self):
        self.rect.move_ip(-1, 0)
        if self.rect.right < 0:
            self.kill()
pantalla = pygame.display.set_mode([pantalla_ancho, pantalla_largo])
pygame.display.set_caption("Proyecto")

Jugador = Jugador()
"""superficie = pygame.Surface((50,50))
superficie.fill((blanco))                             #rellena la pantalla de ese color

rectangulo_de_superficie = superficie.get_rect()   #RECTANGULO DEL OBJETO SUPERFICIE

#PARA OBTENER EL CENTRO DE LA PANTALLA PARA OTRO OBJETO, es calculo matematico noma

centro_superficie = (                                            #SIRVE PARA OBTENER UN BLOQUE RANDOM EN EL MEDIO DE LA PANTALLA XD
    (pantalla_ancho-superficie.get_width())/2,
    (pantalla_largo-superficie.get_height())/2
)
pantalla.blit(superficie, centro_superficie)    #Para meter otra "pantalla" dentro de la anterior pantalla se usa blit
pygame.display.flip()                           # no se para que flip xd"""
condicion = True
while condicion:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            condicion = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                condicion = False
        elif event.type == ADDCLOUD:
            # Create the new cloud and add it to sprite groups
            new_cloud = Cloud()
            clouds.add(new_cloud)
            all_sprites.add(new_cloud)
    teclas_presionadas = pygame.key.get_pressed()

    Jugador.update(teclas_presionadas)

    pantalla.fill(negro)
    pantalla.blit(Jugador.superf, Jugador.rect.topleft)  # Dibuja el jugador en su posición
    pygame.display.update()
    clouds.update()
    pantalla.fill(azul)
pygame.quit()
sys.exit()