import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import random
import time
import math

# Configuraciones iniciales
width, height = 800, 600
max_balls = 10
ball_radius = 0.05
speed = 0.01

# Clase para las bolas
class Ball:
    def __init__(self):
        self.x = random.uniform(-1 + ball_radius, 1 - ball_radius)
        self.y = random.uniform(-1 + ball_radius, 1 - ball_radius)
        self.vx = speed * random.choice([-1, 1])
        self.vy = speed * random.choice([-1, 1])

    def move(self):
        self.x += self.vx
        self.y += self.vy

        # Rebote en las paredes
        if self.x <= -1 + ball_radius or self.x >= 1 - ball_radius:
            self.vx *= -1
        if self.y <= -1 + ball_radius or self.y >= 1 - ball_radius:
            self.vy *= -1

    def draw(self):
        glBegin(GL_TRIANGLE_FAN)
        glVertex2f(self.x, self.y)
        for angle in range(0, 360, 10):
            x = self.x + (ball_radius * math.cos(math.radians(angle)))
            y = self.y + (ball_radius * math.sin(math.radians(angle)))
            glVertex2f(x, y)
        glEnd()

# Inicialización de Pygame y OpenGL
pygame.init()
pygame.display.set_mode((width, height), DOUBLEBUF | OPENGL)
gluOrtho2D(-1, 1, -1, 1)

# Crear bolas
balls = [Ball() for _ in range(max_balls)]

# Bucle principal
running = True
prev_time = time.time()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Actualizar y dibujar bolas
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    for ball in balls:
        ball.move()
        ball.draw()

    # Mostrar framerate
    current_time = time.time()
    fps = 1 / (current_time - prev_time)
    prev_time = current_time
    pygame.display.set_caption(f"FPS: {fps:.2f}")

    pygame.display.flip()
    pygame.time.wait(10)

pygame.quit()
