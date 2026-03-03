import pygame
from grid import Grid
from sand_cell import SandCell
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

COLS, ROWS = 200, 150
CELL_SIZE = 4  # each cell is 4x4 pixels

grid = Grid(COLS, ROWS)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mouse_buttons = pygame.mouse.get_pressed()
    
    if mouse_buttons[0]:
        # This code runs every frame the left button is held down
        x, y = pygame.mouse.get_pos()
        
        if grid.get_cell(int(x/4), int(y/4)) is None:
            grid.add_cell(SandCell(int(x/4), int(y/4)))
        else:
            grid.remove_cell(SandCell(int(x/4), int(y/4)))

    screen.fill((135, 206, 235))  # clear screen
    
    # draw things here
    for y in range(grid.rows - 1, -1, -1):
        for x in range(grid.cols):
            cell = grid.grid[x][y]
            if cell is not None and y != grid.rows - 1 and 0 < x < grid.cols - 1:
                cell.check_rules(grid)
                
                pygame.draw.rect(screen, cell.color, (cell.x * CELL_SIZE, cell.y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    
    pygame.display.flip()
    clock.tick(60)  # 60 FPS

pygame.quit()