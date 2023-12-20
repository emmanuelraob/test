import math
import random
from enum import Enum

from global_use.vec2 import Vec2
from Ants.ants.soldier_ant import Soldier_ant
from Ants.ants.worker_ant import Worker_ant
from Ants.ants.queen import Queen

class State (Enum):
    NEUTRAL = 0
    ATTACK = 1
    DEFENCE = 2
    FOOD_EXPANSION = 3
    ANT_SPACE_EXPANSION = 4
    COLONY_EXPANSION = 5


class Ant_colony:
    def __init__(self, screen, kikgdom_id):

        #state
        self.colony_state = State.NEUTRAL
        self.position = Vec2(random.randint(0, screen.get_size()[0]), random.randint(0, screen.get_size()[1]))
        
        #Food 
        self.max_consumible_food_amount = 10
        self.consumible_food = 0
        self.max_production_food_amount = 10
        self.food_in_production = self.max_production_food_amount
        self.rate_food_convertion = 0 #rate per second

        #Ants
        self.max_ant_amout = 10
        self.ant_amout = 7
        self.ant_generation = 1
        self.soldier_ant_amount = int(self.ant_amout*3/10)
        self.max_worker_ant_amount = int(self.ant_amout*7/10)
        self.out_worker_ant_amount = int(self.max_worker_ant_amount/2)
        self.in_worker_ant_amount = int(self.max_worker_ant_amount/2)
        self.soldiers = {Soldier_ant(self.position,kikgdom_id,self.ant_generation) for _ in range(self.soldier_ant_amount)}
        self.in_workers = {Worker_ant(self.position,kikgdom_id,self.ant_generation) for _ in range(self.in_worker_ant_amount)}
        self.out_workers = {Worker_ant(self.position,kikgdom_id,self.ant_generation) for _ in range(self.out_worker_ant_amount)}
        

        #food and enemy known areas 
        self.food_areas = []
        self.enemy_areas = []

    def draw(self, screen):
        for ant in self.soldiers:
            ant.draw(screen)   

        for ant in self.in_workers:
            ant.draw(screen)   

        for ant in self.out_workers:
            ant.draw(screen)        

    def every_frame_ant_colony_work(self,screen, delta_time):
        #convertir comida en produccion a comida consumible 
        self.every_frame_ants_work(screen, delta_time)


    def every_frame_ants_work(self, screen, delta_time):
        for ant in self.soldiers:
            ant.action(screen, delta_time)

        for ant in self.in_workers:
            ant.action(screen, delta_time)

        for ant in self.out_workers:
            ant.action(screen, delta_time)
        

    def every_second_ant_colony_work(self, screen):
        #verificar el rate de conversion de comida dependiendo de la cantidad maxima de comida consumible
        pass

    def every_week_ant_colony_work(self):
        self.ant_generation += 1

    def verificate_state(self, screen):
        pass
