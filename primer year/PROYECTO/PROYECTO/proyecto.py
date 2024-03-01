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
        #self.rect.topleft = (0, 0)          #SI LO QUIERO EN ARRIBA A LA IZQUIERDA PONER (0,0) y poner self.rect.topleft;
                                            #si arriba a la derecha poner (pantalla_ancho,0) y reemplazar topleft por topright;
                                            #si abajo a la izquierda (0, pantalla_larga) y cambiar topleft por bottomleft;
                                            #si abajo a la derecha (pantalla_ancho, pantalla_larga) y cambiar topleft por bottomright;      
                                    
Jugador = Jugador()

pantalla = pygame.display.set_mode([pantalla_ancho,pantalla_largo])  ###CONFIGURACION DE LA PANTALLA
pygame.display.set_caption("Proyecto")  #NOMBRE DE LA PANTALLA

pantalla.fill(negro)
"""
superficie = pygame.Surface((50,50))
superficie.fill((blanco))                             #rellena la pantalla de ese color

rectangulo_de_superficie = superficie.get_rect()   #RECTANGULO DEL OBJETO SUPERFICIE

#PARA OBTENER EL CENTRO DE LA PANTALLA PARA OTRO OBJETO, es calculo matematico noma

centro_superficie = (                                            SIRVE PARA OBTENER UN BLOQUE RANDOM EN EL MEDIO DE LA PANTALLA XD
    (pantalla_ancho-superficie.get_width())/2,
    (pantalla_largo-superficie.get_height())/2
)
pantalla.blit(superficie, centro_superficie)    #Para meter otra "pantalla" dentro de la anterior pantalla se usa blit
pygame.display.flip()                           # no se para que flip xd"""
x = True
while x:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:           #para salir del juego presionando la x
            x = False
        if event.type == KEYDOWN:                  #detecta si se utilizo alguna tecla
            if event.key == K_ESCAPE:           #lo mismo pero con el escape
                x = False
    pantalla.blit(Jugador.superf, (pantalla_ancho/2, pantalla_largo/2))
    pygame.display.update()