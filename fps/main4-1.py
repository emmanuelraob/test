import pygame
import random
import time
import threading

# Inicialización de Pygame
pygame.init()

# Configurar pantalla
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bolas rebotando")

# Colores
BLACK = (0, 0, 0)

# Configuraciones de las bolas
max_balls = 10
ball_radius = 20
speed = 300  # Velocidad en píxeles por segundo

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

        # Rebote en las paredes teniendo en cuenta el radio de la bola
        if self.x - ball_radius <= 0 or self.x + ball_radius >= width:
            self.vx *= -1
            self.x = max(ball_radius, min(self.x, width - ball_radius))

        if self.y - ball_radius <= 0 or self.y + ball_radius >= height:
            self.vy *= -1
            self.y = max(ball_radius, min(self.y, height - ball_radius))

    def draw(self):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), ball_radius)

def update_ball_positions(balls, dt):
    for ball in balls:
        ball.move(dt)

# Crear bolas
balls = [Ball() for _ in range(max_balls)]

# Bucle principal
running = True
last_time = time.perf_counter()
frame_count = 0
accumulated_time = 0
ball_thread = None

while running:
    current_time = time.perf_counter()
    dt = current_time - last_time
    last_time = current_time

    if ball_thread is None or not ball_thread.is_alive():
        # Iniciar un nuevo hilo para actualizar las posiciones de las bolas
        ball_thread = threading.Thread(target=update_ball_positions, args=(balls, dt))
        ball_thread.start()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Dibujar bolas
    screen.fill(BLACK)
    for ball in balls:
        ball.draw()
    pygame.display.flip()

    # Actualizar FPS
    accumulated_time += dt
    frame_count += 1
    if accumulated_time >= 1.0:
        fps = frame_count / accumulated_time
        pygame.display.set_caption(f"Bolas rebotando - FPS: {fps:.0f}")
        frame_count = 0
        accumulated_time = 0

pygame.quit()
