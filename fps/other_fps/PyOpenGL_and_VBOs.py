import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.arrays import vbo
from OpenGL.GLU import *
import random
import time
import numpy as np

# Configuraciones iniciales
width, height = 800, 600
max_balls = 10000
ball_radius = 0.002
speed = 0.01

# Clase para las bolas
class Ball:
    def __init__(self, radius, speed, width, height):
        self.radius = radius
        self.speed = speed
        self.width = width
        self.height = height
        self.x = random.uniform(-1 + radius, 1 - radius)
        self.y = random.uniform(-1 + radius, 1 - radius)
        self.vx = speed * random.choice([-1, 1])
        self.vy = speed * random.choice([-1, 1])

        # Crear un cuadrado (rectángulo) como VBO
        self.vbo = vbo.VBO(
            np.array([
                [self.x - radius, self.y - radius],
                [self.x + radius, self.y - radius],
                [self.x + radius, self.y + radius],
                [self.x - radius, self.y + radius]
            ], dtype='float32')
        )

    def move(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt

        # Actualizar VBO
        new_vertices = np.array([
            [self.x - self.radius, self.y - self.radius],
            [self.x + self.radius, self.y - self.radius],
            [self.x + self.radius, self.y + self.radius],
            [self.x - self.radius, self.y + self.radius]
        ], dtype='float32')
        self.vbo.set_array(new_vertices)

    def draw(self):
        self.vbo.bind()
        glEnableClientState(GL_VERTEX_ARRAY)
        glVertexPointerf(self.vbo)
        glDrawArrays(GL_QUADS, 0, 4)
        self.vbo.unbind()
        glDisableClientState(GL_VERTEX_ARRAY)

# Inicialización de Pygame y OpenGL
pygame.init()
pygame.display.set_mode((width, height), DOUBLEBUF | OPENGL)
gluOrtho2D(-1, 1, -1, 1)

# Crear bolas
balls = [Ball(ball_radius,speed,width,height) for _ in range(max_balls)]

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
