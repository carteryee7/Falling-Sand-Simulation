from models.cell import Cell

class Grid:
    def __init__(self, cols, rows):
        self.cols = cols
        self.rows = rows
        self.grid: list[list[Cell]] = [[None for _ in range(rows)] for _ in range(cols)]

    def add_cell(self, cell: Cell):
        if 0 <= cell.x < self.cols and 0 <= cell.y < self.rows:
            self.grid[cell.x][cell.y] = cell
    
    def remove_cell(self, x, y):
        if 0 <= x < self.cols and 0 <= y < self.rows:
            self.grid[x][y] = None

    def set_cell_pos(self, cell: Cell, new_x, new_y):
        if 0 <= new_x < self.cols and 0 <= new_y < self.rows:
            self.grid[cell.x][cell.y] = None  # Clear old position
            cell.x = new_x
            cell.y = new_y
            self.grid[new_x][new_y] = cell  # Set new position
    
    def swap_pos(self, cell: Cell, new_cell: Cell):
        if 0 <= new_cell.x < self.cols and 0 <= new_cell.y < self.rows:
            # Store the positions
            x1, y1 = cell.x, cell.y
            x2, y2 = new_cell.x, new_cell.y
            
            # Swap positions in grid
            self.grid[x1][y1] = new_cell
            self.grid[x2][y2] = cell
            
            # Update cell coordinates
            cell.x, cell.y = x2, y2
            new_cell.x, new_cell.y = x1, y1

    def get_cell(self, x, y):
        if 0 <= x < self.cols and 0 <= y < self.rows:
            return self.grid[x][y]
        return None