from models.cell import Cell
from grid import Grid

class  BedrockCell(Cell):
    def __init__(self, x, y):
        color = (0, 0, 0)
        super().__init__(color, x, y)
    
    def check_rules(self, grid: Grid):
        pass