from abc import ABC, abstractmethod

class Cell(ABC):
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y
    
    @abstractmethod
    def check_rules(self):
        pass