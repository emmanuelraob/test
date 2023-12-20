from Ants.ants.ant import Ant
from global_use.colors import Colors

colors = Colors()

class Soldier_ant(Ant):
    def __init__(self,position, kikgdom_id):
        super().__init__(position)
        self.color = colors.kingdom_ant_color[kikgdom_id]
        self.radious = 2
        

