import random 
from Ants.ants.ant import Ant
from global_use.colors import Colors
from enum import Enum
from Ants.ants.ant import State
from global_use.vec2 import Vec2


colors = Colors()

class Worker_ant(Ant):
    def __init__(self, position, kikgdom_id, generation):
        
        # position and movement
        self.speed = random.uniform(0.5, 0.8) #in pixels per second
        self.velocity = Vec2(self.speed * random.uniform(-1, 1),self.speed * random.uniform(-1, 1)) 
        self.position = Vec2(position.x + random.randint(-2, 2), position.y + random.randint(-2, 2))


        #food and energy   
        self.weight = 1
        self.max_energy = 10
        self.food = 5 
        self.max_food = 5
        self.water = 5
        self.max_water = 5

        #load 
        self.load = self.food
        self.max_load = 50

        #attack and life
        self.attack_damage = 1
        self.life = 10   
        self.max_life = 10  
        self.age = 0   
        self.max_age = random.randint(10,15) 


        #states and caracteristics
        self.state = State.LOOKING_FOR_FOOD
        self.generation = generation
        self.color = colors.kingdom_ant_color[kikgdom_id]
        self.radious = 1


        
        

