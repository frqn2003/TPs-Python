import pygame
import sys

pygame.init()

# Configuración de la pantalla
ancho_pantalla = 800
largo_pantalla = 600
pantalla = pygame.display.set_mode((ancho_pantalla, largo_pantalla))
pygame.display.set_caption("Juego de Decisiones")

# Bucle principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Lógica del juego y actualizaciones aquí

    # Dibujar en la pantalla
    pantalla.fill((255, 255, 255))  # Rellenar la pantalla con blanco (puedes cambiarlo a otro color)
    # Dibujar otros elementos aquí

    pygame.display.flip()  # Actualizar la pantalla
