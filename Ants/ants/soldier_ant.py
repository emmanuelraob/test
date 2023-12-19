from Ants.ants.ant import Ant

class Soldier_ant(Ant):
    def __init__(self,position, color):
        super().__init__(position)
        self.color = color
        

