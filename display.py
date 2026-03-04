import pygame
from grid import Grid
from models.sand_cell import SandCell
from models.water_cell import WaterCell
from models.stone_cell import StoneCell
from models.steam_cell import SteamCell
from models.bedrock_cell import BedrockCell
from models.button import Button

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

COLS, ROWS = 200, 150
CELL_SIZE = 4  # each cell is 4x4 pixels

grid = Grid(COLS, ROWS)

input = "sand"
sand_butt = Button("Sand", (194, 178, 128), (0, 0, 0), 750, 150, 40, 40)
water_butt = Button("Water", (0, 0, 255), (0, 0, 0), 750, 190, 40, 40)
stone_butt = Button("Stone", (128, 128, 128), (0, 0, 0), 750, 230, 40, 40)
steam_butt = Button("Steam", (211, 211, 211), (0, 0, 0), 750, 270, 40, 40)
bedrock_butt = Button("Bedrock", (0, 0, 0), (255, 255, 255), 750, 310, 40, 40)
eraser_butt = Button("Eraser", (255, 255, 255), (0, 0, 0), 750, 350, 40, 40)
reset_butt = Button("Reset", (255, 0, 0), (0, 0, 0), 750, 390, 40, 40)

border = pygame.Rect(750, 150, 280, 40)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # keyboard input
        """
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
                input = "eraser"
            if event.key == pygame.K_r:
                grid = Grid(COLS, ROWS)  # reset grid
        """
        # button input
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if sand_butt.rect.collidepoint(x, y):
                input = "sand"
            if water_butt.rect.collidepoint(x, y):
                input = "water"
            if stone_butt.rect.collidepoint(x, y):
                input = "stone"
            if steam_butt.rect.collidepoint(x, y):
                input = "steam"
            if bedrock_butt.rect.collidepoint(x, y):
                input = "bedrock"
            if eraser_butt.rect.collidepoint(x, y):
                input = "eraser"
            if reset_butt.rect.collidepoint(x, y):
                grid = Grid(COLS, ROWS)  # reset grid

    mouse_buttons = pygame.mouse.get_pressed()
    
    if mouse_buttons[0]:
        # This code runs every frame the left button is held down
        x, y = pygame.mouse.get_pos()
        if not border.collidepoint(x, y):
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
                if input == "eraser":
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
    
    sand_butt.draw(screen)
    water_butt.draw(screen)
    stone_butt.draw(screen)
    steam_butt.draw(screen)
    bedrock_butt.draw(screen)
    eraser_butt.draw(screen)
    reset_butt.draw(screen)
    pygame.display.flip()
    clock.tick(60)  # 60 FPS

pygame.quit()