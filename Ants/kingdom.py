import random

from Ants.ant_colony import Ant_colony



class Kingdom:
    def __init__(self, screen, kingdom_id, colonies_amount):
        self.colonies = {Ant_colony(screen, kingdom_id) for _ in range(colonies_amount)}

        
    def draw(self, screen):
        for colony in self.colonies:
            colony.draw(screen)

    def every_frame_kingdom_work(self, screen, delta_time):
        for colony in self.colonies:
            colony.every_frame_ant_colony_work(screen, delta_time)
    
    def every_second_kingdom_work(self, screen):
        for colony in self.colonies:
            colony.every_second_ant_colony_work(screen)

