import pygame
from grid import Grid
from models.sand_cell import SandCell
from models.water_cell import WaterCell
from models.stone_cell import StoneCell
from models.steam_cell import SteamCell
from models.bedrock_cell import BedrockCell

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

COLS, ROWS = 200, 150
CELL_SIZE = 4  # each cell is 4x4 pixels

grid = Grid(COLS, ROWS)

input = "sand"

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                input = "sand"
            if event.key == pygame.K_2:
                input = "water"
            if event.key == pygame.K_3:
                input = "stone"
            if event.key == pygame.K_4:
                input = "steam"
            if event.key == pygame.K_5:
                input = "bedrock"
            if event.key == pygame.K_e:
                input = "erase"
            if event.key == pygame.K_r:
                grid = Grid(COLS, ROWS)  # reset grid

    mouse_buttons = pygame.mouse.get_pressed()
    
    if mouse_buttons[0]:
        # This code runs every frame the left button is held down
        x, y = pygame.mouse.get_pos()
        
        if grid.get_cell(int(x/4), int(y/4)) is None:
            match input:
                case "sand":
                    grid.add_cell(SandCell(int(x/4), int(y/4)))
                case "water":
                    grid.add_cell(WaterCell(int(x/4), int(y/4)))
                case "stone":
                    grid.add_cell(StoneCell(int(x/4), int(y/4)))
                case "steam":
                    grid.add_cell(SteamCell(int(x/4), int(y/4)))
                case "bedrock":
                    grid.add_cell(BedrockCell(int(x/4), int(y/4)))
        else:
            if input == "erase":
                grid.remove_cell(int(x/4), int(y/4))

    screen.fill((135, 206, 235))  # clear screen
    
    # draw things here
    if input == "steam" or input == "erase":
        for y in range(grid.rows):
            for x in range(grid.cols):
                cell = grid.grid[x][y]
                if cell is not None and y != grid.rows - 1 and 0 < x < grid.cols - 1:
                    cell.check_rules(grid)
                    
                    pygame.draw.rect(screen, cell.color, (cell.x * CELL_SIZE, cell.y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    else:
        for y in range(grid.rows - 1, -1, -1):
            for x in range(grid.cols):
                cell = grid.grid[x][y]
                if cell is not None and y != grid.rows - 1 and 0 < x < grid.cols - 1:
                    cell.check_rules(grid)
                    
                    pygame.draw.rect(screen, cell.color, (cell.x * CELL_SIZE, cell.y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    
    pygame.display.flip()
    clock.tick(60)  # 60 FPS

pygame.quit()