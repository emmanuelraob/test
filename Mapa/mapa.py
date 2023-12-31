import numpy as np
import pygame



class Mapa:
    def __init__(self, width, height, section_area):
        self.width = width
        self.height = height
        self.section_area = section_area
        self.walls = np.zeros((int(height / section_area), int(width / section_area)))

    def draw(self, screen):
        for y in range(len(self.walls)):
            for x in range(len(self.walls[y])):
                rect = pygame.Rect(x * self.section_area, y * self.section_area, self.section_area, self.section_area)
                color = (255, 255, 255) if self.walls[y][x] == 1 else (0, 0, 0)
                pygame.draw.rect(screen, color, rect)

    def update_cell(self, pos):
        x, y = pos
        grid_x, grid_y = x // self.section_area, y // self.section_area
        self.walls[grid_y, grid_x] = 1

# Inicializar Pygame y crear ventana
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

# Crear instancia de Mapa
mapa = Mapa(1280, 720, 5)

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Actualizar celda en la que se hizo clic
            mapa.update_cell(pygame.mouse.get_pos())

    # Dibujar la cuadrícula
    screen.fill((0, 0, 0))  # Limpiar pantalla
    mapa.draw(screen)

    pygame.display.flip()  # Actualizar la pantalla
    clock.tick(60)  # 60 FPS

pygame.quit()


