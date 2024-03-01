import pygame, sys

#Inicializo la pantalla
pygame.init

blanco = (255,255,255) ###COLORES
negro = (0,0,0)
azul = (53,79,194)
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,                                       ####TECLAS DEL JUEGO####
    K_SPACE,
    KEYDOWN,
    QUIT,
)

pantalla_ancho = 800
pantalla_largo = 600

class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super(Jugador, self).__init__()
        self.superf = pygame.Surface((75, 25))
        self.superf.fill((azul))
        self.rect = self.superf.get_rect()
        self.rect.topleft = (pantalla_ancho/2, pantalla_largo/2)          #SI LO QUIERO EN ARRIBA A LA IZQUIERDA PONER (0,0) y poner self.rect.topleft;
                                            #si arriba a la derecha poner (pantalla_ancho,0) y reemplazar topleft por topright;
                                            #si abajo a la izquierda (0, pantalla_larga) y cambiar topleft por bottomleft;
                                            #si abajo a la derecha (pantalla_ancho, pantalla_larga) y cambiar topleft por bottomright;      
    def update(self, teclas_presionadas):
        if teclas_presionadas[K_UP]:
            self.rect.move_ip(0,-5)
        if teclas_presionadas[K_DOWN]:
            self.rect.move_ip(0,5)
        if teclas_presionadas[K_LEFT]:
            self.rect.move_ip(-5,0)
        if teclas_presionadas[K_RIGHT]:
            self.rect.move_ip(5,0)                            

pantalla = pygame.display.set_mode([pantalla_ancho,pantalla_largo])  ###CONFIGURACION DE LA PANTALLA
pygame.display.set_caption("Proyecto")  #NOMBRE DE LA PANTALLA

Jugador = Jugador()
x = True
while x:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:           #para salir del juego presionando la x
            x = False
        if event.type == KEYDOWN:                  #detecta si se utilizo alguna tecla
            if event.key == K_ESCAPE:           #lo mismo pero con el escape
                x = False
    teclas_presionadas = pygame.key.get_pressed()

    Jugador.update(teclas_presionadas)
    
    pantalla.blit(Jugador.superf, Jugador.rect.topleft)
    pygame.display.update()
pygame.quit()
sys.exit()