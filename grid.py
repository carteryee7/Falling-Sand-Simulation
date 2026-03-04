from models.cell import Cell

class Grid:
    def __init__(self, cols, rows):
        """Initialize a new grid with specified dimensions.
        
        Args:
            cols: Number of columns in the grid
            rows: Number of rows in the grid
        """
        self.cols = cols
        self.rows = rows
        self.grid: list[list[Cell]] = [[None for _ in range(rows)] for _ in range(cols)]

    def add_cell(self, cell: Cell):
        """Add a cell to the grid at its current position.
        
        Args:
            cell: The cell to add to the grid
        """
        if 0 <= cell.x < self.cols and 0 <= cell.y < self.rows:
            self.grid[cell.x][cell.y] = cell
    
    def remove_cell(self, x, y):
        """Remove a cell from the grid at the specified position.
        
        Args:
            x: The x-coordinate of the cell to remove
            y: The y-coordinate of the cell to remove
        """
        if 0 <= x < self.cols and 0 <= y < self.rows:
            self.grid[x][y] = None

    def set_cell_pos(self, cell: Cell, new_x, new_y):
        """Move a cell to a new position in the grid.
        
        Args:
            cell: The cell to move
            new_x: The new x-coordinate
            new_y: The new y-coordinate
        """
        if 0 <= new_x < self.cols and 0 <= new_y < self.rows:
            self.grid[cell.x][cell.y] = None  # Clear old position
            cell.x = new_x
            cell.y = new_y
            self.grid[new_x][new_y] = cell  # Set new position
    
    def swap_pos(self, cell: Cell, new_cell: Cell):
        """Swap the positions of two cells in the grid.
        
        Args:
            cell: The first cell to swap
            new_cell: The second cell to swap with
        """
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
        """Get the cell at the specified position.
        
        Args:
            x: The x-coordinate
            y: The y-coordinate
            
        Returns:
            The cell at the position, or None if position is empty or out of bounds
        """
        if 0 <= x < self.cols and 0 <= y < self.rows:
            return self.grid[x][y]
        return None