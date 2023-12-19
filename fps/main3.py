import pygame
import random
import time

# Inicialización de Pygame
pygame.init()

# Configurar pantalla
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

# Colores
BLACK = (0, 0, 0)

# Configuraciones de las bolas
max_balls = 10
ball_radius = 20
speed = 0.3  # Velocidad en píxeles por milisegundo

# Clase para las bolas
class Ball:
    def __init__(self):
        self.x = random.randint(ball_radius, width - ball_radius)
        self.y = random.randint(ball_radius, height - ball_radius)
        self.vx = speed * random.choice([-1, 1])
        self.vy = speed * random.choice([-1, 1])
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def move(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt

        # Rebote en las paredes
        if self.x <= ball_radius or self.x >= width - ball_radius:
            self.vx *= -1
        if self.y <= ball_radius or self.y >= height - ball_radius:
            self.vy *= -1

    def draw(self):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), ball_radius)

# Crear bolas
balls = [Ball() for _ in range(max_balls)]

# Inicializar reloj para medir FPS
clock = pygame.time.Clock()

# Bucle principal
running = True
last_time = pygame.time.get_ticks()

while running:
    current_time = pygame.time.get_ticks()
    dt = current_time - last_time
    last_time = current_time

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Actualizar y dibujar bolas
    screen.fill(BLACK)
    for ball in balls:
        ball.move(dt)
        ball.draw()

    pygame.display.flip()

    # Espera mínima para evitar consumo excesivo de CPU
    pygame.time.wait(1)

pygame.quit()
