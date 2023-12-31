# ball.pyx
cimport cython
from libc.stdlib cimport rand
from libc.limits cimport INT_MAX  # Importar INT_MAX
from libc.math cimport M_PI, cos, sin

@cython.boundscheck(False)
@cython.wraparound(False)
cdef class Ball:
    cdef public float x, y, vx, vy, width, height, radius, speed

    def __init__(self, float radius, float speed):
        self.radius = radius
        self.speed = speed
        self.width = radius * 2
        self.height = radius * 2
        self.x = (rand() / <float>INT_MAX) * (2 - self.width) - 1 + self.radius
        self.y = (rand() / <float>INT_MAX) * (2 - self.height) - 1 + self.radius
        self.vx = speed * ((rand() % 2) * 2 - 1)
        self.vy = speed * ((rand() % 2) * 2 - 1)

    cpdef move(self, float dt):
        self.x += self.vx * dt
        self.y += self.vy * dt

        # Rebote en las paredes teniendo en cuenta el tamaño del rectángulo
        if self.x - self.width / 2 <= -1 or self.x + self.width / 2 >= 1:
            self.vx *= -1
            self.x = max(-1 + self.width / 2, min(self.x, 1 - self.width / 2))

        if self.y - self.height / 2 <= -1 or self.y + self.height / 2 >= 1:
            self.vy *= -1
            self.y = max(-1 + self.height / 2, min(self.y, 1 - self.height / 2))
