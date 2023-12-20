import random 
import pygame
import math
from enum import Enum

from global_use.vec2 import Vec2

class State (Enum):
    LOOKING_FOR_FOOD = 0
    EATING = 1
    


class Ant:
    def __init__(self, position):
        # position and movement
        self.speed = random.uniform(0.5, 1.5) #in pixels per second
        self.velocity = Vec2(self.speed * random.uniform(-1, 1),self.speed * random.uniform(-1, 1)) 
        self.position = Vec2(position.x + random.randint(-2, 2), position.y + random.randint(-2, 2))
        
        
        #food and energy        
        self.weight = 0  
        self.max_energy = 0
        self.food = 0   
        self.max_food = 0  
        self.water = 0  
        self.max_water = 0  

        #load 
        self.load = 0   
        self.max_load = 0  
        
        #attack and life
        self.attack_damage = 0  
        self.life = 0   
        self.max_life = 0  
        self.age = 0   
        self.max_age = 0  

        #states and caracteristics 
        self.state = State.LOOKING_FOR_FOOD  
        self.generation = 0  
        self.color = (255,255,255)
        self.radious = 1


    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.position.x, self.position.y), self.radious)

    def action(self, screen, delta_time):
        self.move(screen, delta_time)
        pass

    def move(self, screen, delta_time):
        screen_width = screen.get_size()[0]
        screen_height = screen.get_size()[1]

        self.position.x += self.velocity.x * delta_time * 30
        self.position.y += self.velocity.y * delta_time * 30

        # Rebote en las paredes teniendo en cuenta el radio de la bola
        if self.position.x - self.radious <= 0 or self.position.x + self.radious >= screen_width:
            self.velocity.x *= -1
            # Corrige la posición para que la bola no se "pegue" al borde
            self.position.x = max(self.radious, min(self.position.x, screen_width - self.radious))

        if self.position.y - self.radious <= 0 or self.position.y + self.radious >= screen_height:
            self.velocity.y *= -1
            # Corrige la posición para que la bola no se "pegue" al borde
            self.position.y = max(self.radious, min(self.position.y, screen_height - self.radious))


    def think(self):
        pass


        

