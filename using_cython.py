import os
import sys
import subprocess
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import time

def build_cython_modules():
    # Comprueba si los archivos .pyx han sido modificados más recientemente que sus .c correspondientes
    need_rebuild = False
    cython_files = ["ball.pyx"]
    for file in cython_files:
        c_file = file.replace('.pyx', '.c')
        if (not os.path.exists(c_file) or
            os.path.getmtime(file) > os.path.getmtime(c_file)):
            need_rebuild = True
            break

    # Si es necesario, recompila los módulos Cython
    if need_rebuild:
        print("Recompilando módulos Cython...")
        subprocess.run([sys.executable, "setup.py", "build_ext", "--inplace"])

build_cython_modules()

import ball  # Asegúrate de que este módulo esté compilado y disponible

# Configuraciones iniciales
width, height = 800, 600
max_balls = 1000
ball_radius = 1/width * 2
speed = 1/width * 3

# Inicialización de Pygame y OpenGL
pygame.init()
pygame.display.set_mode((width, height), DOUBLEBUF | OPENGL)
gluOrtho2D(-1, 1, -1, 1)

# Crear bolas
balls = [ball.Ball(ball_radius, speed) for _ in range(max_balls)]

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
    for b in balls:
        b.move(dt)
        glBegin(GL_QUADS)
        glVertex2f(b.x - b.width / 2, b.y - b.height / 2)
        glVertex2f(b.x + b.width / 2, b.y - b.height / 2)
        glVertex2f(b.x + b.width / 2, b.y + b.height / 2)
        glVertex2f(b.x - b.width / 2, b.y + b.height / 2)
        glEnd()

    # Mostrar framerate cada segundo
    if accum_time >= 1.0:
        fps = frame_count / accum_time
        pygame.display.set_caption(f"FPS: {fps:.2f}")
        frame_count = 0
        accum_time = 0

    pygame.display.flip()

pygame.quit()
