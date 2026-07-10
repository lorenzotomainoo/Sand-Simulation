import random
import pygame

BLACK_CELL_COLOR = (10, 10, 10)

cell_state = {
    "Empty": 0,
    "Sand": 1,
    "Water": 2,
    "Dirt": 3
}

class Cell:
    def __init__(self):
        self.color = (0, 0, 0)
        self.state = cell_state["Empty"]

def init_matrix(width, height, cell_size):
    cell_x = int(width / cell_size)
    cell_y = int(height / cell_size)
    ret = []
    
    for _ in range(cell_x):
        t = []
        for _ in range(cell_y):
            t.append(Cell())
        ret.append(t)
    return ret

def reset_matrix(matrix, width, height, cell_size):
    cell_x = int(width / cell_size)
    cell_y = int(height / cell_size)
    
    for i in range(cell_x):
        for j in range(cell_y):
            matrix[i][j].state = cell_state["Empty"]
            matrix[i][j].color = BLACK_CELL_COLOR

def draw_matrix(screen, matrix, height, width, cell_size):
    cell_x = int(width / cell_size)
    cell_y = int(height / cell_size)
    
    for i in range(cell_x):
        for j in range(cell_y):
            if matrix[i][j].state == cell_state["Empty"]:
                rect = (i * cell_size, j * cell_size, cell_size, cell_size)
                pygame.draw.rect(screen, BLACK_CELL_COLOR, rect, 1)
            else:
                rect = (i * cell_size, j * cell_size, cell_size, cell_size)
                pygame.draw.rect(screen, matrix[i][j].color, rect)
                
def init_color(toggle):
    if toggle == 1:
        return (random.randint(180, 240), random.randint(140, 210), random.randint(70, 140)) #! sand
    if toggle == 2:
        return (random.randint(0, 50), random.randint(100, 200), random.randint(180, 255)) #! water
    if toggle == 3:
        return (random.randint(90, 140), random.randint(50, 90), random.randint(20, 50)) #! dirt
    if toggle == 4:
        return BLACK_CELL_COLOR

def draw_sand(matrix, c: tuple, cell_size, toggle, brush_radius = 2):
    center_x = int(c[0] / cell_size) 
    center_y = int(c[1] / cell_size)        
    
    for dx in range(-brush_radius, brush_radius + 1):
        for dy in range(-brush_radius, brush_radius + 1):
            
            if dx**2 + dy**2 <= brush_radius**2:
                nx = center_x + dx
                ny = center_y + dy
    
                if 0 <= nx < len(matrix) and 0 <= ny < len(matrix[0]):
                    cell = matrix[nx][ny]
                    
                    if toggle == 4: 
                        cell.state = cell_state["Empty"]
                        cell.color = BLACK_CELL_COLOR
                
                    elif cell.state == cell_state["Empty"]:
                        cell.color = init_color(toggle)
                        
                        if toggle == 1:
                            cell.state = cell_state["Sand"]
                        elif toggle == 2:
                            cell.state = cell_state["Water"]
                        elif toggle == 3:
                            cell.state = cell_state["Dirt"]
            
def update_sand(matrix):
    for y in reversed(range(len(matrix[0]))):
        for x in range(len(matrix)):
            
            if y == len(matrix[0]) - 1: 
                continue
            
            if matrix[x][y].state != cell_state["Empty"]:
                color = matrix[x][y].color
                state = matrix[x][y].state
                
                if matrix[x][y + 1].state == cell_state["Empty"]:
                    matrix[x][y + 1].state = state
                    matrix[x][y + 1].color = color
                    
                    matrix[x][y].state = cell_state["Empty"]
                    matrix[x][y].color = BLACK_CELL_COLOR
                
                elif matrix[x][y + 1].state != cell_state["Empty"]:
                    
                    can_go_left = (x > 0) and (matrix[x - 1][y + 1].state == cell_state["Empty"])
                    can_go_right = (x < len(matrix) - 1) and (matrix[x + 1][y + 1].state == cell_state["Empty"])
                    
                    if can_go_left and not can_go_right:
                        matrix[x - 1][y + 1].state = state
                        matrix[x - 1][y + 1].color = color
                        matrix[x][y].state = cell_state["Empty"]
                        matrix[x][y].color = BLACK_CELL_COLOR
                        
                    elif can_go_right and not can_go_left:
                        matrix[x + 1][y + 1].state = state
                        matrix[x + 1][y + 1].color = color
                        matrix[x][y].state = cell_state["Empty"]
                        matrix[x][y].color = BLACK_CELL_COLOR
                    
                    elif can_go_left and can_go_right:
                        if random.choice([True, False]):
                            matrix[x - 1][y + 1].state = state
                            matrix[x - 1][y + 1].color = color
                        else:
                            matrix[x + 1][y + 1].state = state
                            matrix[x + 1][y + 1].color = color
                            
                        matrix[x][y].state = cell_state["Empty"]
                        matrix[x][y].color = BLACK_CELL_COLOR