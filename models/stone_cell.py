from models.cell import Cell
from grid import Grid
from models.water_cell import WaterCell

class StoneCell(Cell):
    def __init__(self, x, y):
        color = (128, 128, 128)
        super().__init__(color, x, y)
    
    def check_rules(self, grid: Grid):
        if grid.grid[self.x][self.y + 1] is None:
            grid.set_cell_pos(self, self.x, self.y + 1)

        elif isinstance(grid.grid[self.x][self.y + 1], WaterCell):
            grid.swap_pos(self, grid.grid[self.x][self.y + 1])