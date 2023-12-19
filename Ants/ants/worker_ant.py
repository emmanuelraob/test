from Ants.ants.ant import Ant

class Worker_ant(Ant):
    def __init__(self, position, color):
        super().__init__(position)
        self.color = color
        

