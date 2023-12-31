import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import random
import time
import math

# Configuraciones iniciales
width, height = 800, 600
max_balls = 10000
ball_radius = 0.002
speed = 0.01

# Clase para las bolas
class Ball:
    def __init__(self):
        self.x = random.uniform(-1 + ball_radius, 1 - ball_radius)
        self.y = random.uniform(-1 + ball_radius, 1 - ball_radius)
        self.vx = speed * random.choice([-1, 1])
        self.vy = speed * random.choice([-1, 1])
        self.width = ball_radius * 2
        self.height = ball_radius * 2

    def move(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt

        # Rebote en las paredes teniendo en cuenta el tamaño del rectángulo
        if self.x - self.width / 2 <= -1 or self.x + self.width / 2 >= 1:
            self.vx *= -1
            self.x = max(-1 + self.width / 2, min(self.x, 1 - self.width / 2))

        if self.y - self.height / 2 <= -1 or self.y + self.height / 2 >= 1:
            self.vy *= -1
            self.y = max(-1 + self.height / 2, min(self.y, 1 - self.height / 2))

    def draw(self):
        glBegin(GL_QUADS)
        glVertex2f(self.x - self.width / 2, self.y - self.height / 2)
        glVertex2f(self.x + self.width / 2, self.y - self.height / 2)
        glVertex2f(self.x + self.width / 2, self.y + self.height / 2)
        glVertex2f(self.x - self.width / 2, self.y + self.height / 2)
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
frame_count = 0
accum_time = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    current_time = time.time()
    dt = current_time - prev_time
    prev_time = current_time
    accum_time += dt
    frame_count += 1

    # Actualizar y dibujar bolas
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    for ball in balls:
        ball.move(dt)
        ball.draw()

    # Mostrar framerate cada segundo
    if accum_time >= 1.0:
        fps = frame_count / accum_time
        pygame.display.set_caption(f"FPS: {fps:.2f}")
        frame_count = 0
        accum_time = 0

    pygame.display.flip()

pygame.quit()
