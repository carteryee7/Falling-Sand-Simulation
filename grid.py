from cell import Cell

class Grid:
    def __init__(self, cols, rows):
        self.cols = cols
        self.rows = rows
        self.grid: list[list[Cell]] = [[None for _ in range(rows)] for _ in range(cols)]

    def add_cell(self, cell: Cell):
        if 0 <= cell.x < self.cols and 0 <= cell.y < self.rows:
            self.grid[cell.x][cell.y] = cell
    
    def remove_cell(self, cell: Cell):
        if 0 <= cell.x < self.cols and 0 <= cell.y < self.rows:
            self.grid[cell.x][cell.y] = None

    def set_cell_pos(self, cell: Cell, new_x, new_y):
        if 0 <= new_x < self.cols and 0 <= new_y < self.rows:
            self.grid[cell.x][cell.y] = None  # Clear old position
            cell.x = new_x
            cell.y = new_y
            self.grid[new_x][new_y] = cell  # Set new position

    def get_cell(self, x, y):
        if 0 <= x < self.cols and 0 <= y < self.rows:
            return self.grid[x][y]
        return None