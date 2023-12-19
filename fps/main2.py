import pygame
import random
import time

# Inicializar Pygame
pygame.init()

# Configurar pantalla
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bolas rebotando")

# Colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Configuraciones de las bolas
max_balls = 10
ball_radius = 20
speed = 3

# Clase para las bolas
class Ball:
    def __init__(self):
        self.x = random.randint(ball_radius, width - ball_radius)
        self.y = random.randint(ball_radius, height - ball_radius)
        self.vx = speed * random.choice([-1, 1])
        self.vy = speed * random.choice([-1, 1])
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def move(self):
        self.x += self.vx
        self.y += self.vy

        # Rebote en las paredes
        if self.x <= ball_radius or self.x >= width - ball_radius:
            self.vx *= -1
        if self.y <= ball_radius or self.y >= height - ball_radius:
            self.vy *= -1

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), ball_radius)

# Crear bolas
balls = [Ball() for _ in range(max_balls)]

# Bucle principal
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Actualizar y dibujar bolas
    screen.fill(BLACK)
    for ball in balls:
        ball.move()
        ball.draw()

    # Mostrar framerate
    fps = clock.get_fps()
    pygame.display.set_caption(f"Bolas rebotando - FPS: {fps:.2f}")

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
