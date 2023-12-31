import pygame
import math

class Hormiga:
    def __init__(self, x, y, ancho, alto, area_busqueda, direccion, angulo_vision, section_area):
        self.x = x
        self.y = y
        self.ancho = ancho
        self.alto = alto
        self.area_busqueda = area_busqueda
        self.direccion = direccion  # En grados
        self.angulo_vision = angulo_vision  # En grados
        self.section_area = section_area

    def dibujar(self, superficie, font):
        # Dibujar la hormiga
        pygame.draw.rect(superficie, (0, 255, 0), (self.x, self.y, self.ancho, self.alto))

        # Dibujar el campo de visión
        inicio_angulo = self.direccion - self.angulo_vision / 2
        fin_angulo = self.direccion + self.angulo_vision / 2
        puntos = [(self.x + self.ancho / 2, self.y + self.alto / 2)]

        for angulo in range(int(inicio_angulo), int(fin_angulo)):
            rad = math.radians(angulo)
            x = self.x + self.ancho / 2 + self.area_busqueda * math.cos(rad)
            y = self.y + self.alto / 2 + self.area_busqueda * math.sin(rad)
            puntos.append((x, y))

        puntos.append((self.x + self.ancho / 2, self.y + self.alto / 2))
        pygame.draw.polygon(superficie, (255, 0, 0, 128), puntos)

        # Calcular la fila y la columna de la cuadrícula donde está la hormiga
        columna = int((self.x + self.ancho / 2) / self.section_area)
        fila = int((self.y + self.alto / 2) / self.section_area)

        # Dibujar las coordenadas de la cuadrícula en la pantalla
        texto = font.render(f'Fila: {fila}, Columna: {columna}', True, (255, 255, 255))
        superficie.blit(texto, (10, 10))  # Puedes cambiar la posición según sea necesario

    def mover(self):
        # Lógica de movimiento
        pass


# Inicialización de Pygame y creación de la ventana
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 24)  # Crear un objeto Font

# Crear una hormiga
section_area = 5  # Asumiendo que conoces el tamaño de la sección
hormiga = Hormiga(100, 100, 20, 20, 50, 0, 90, section_area)

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # ... lógica para mover la hormiga ...

    # Dibujar todo
    screen.fill((0, 0, 0))
    hormiga.dibujar(screen, font)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

