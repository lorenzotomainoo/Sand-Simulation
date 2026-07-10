import pygame
import library

WIDTH, HEIGHT = 1200, 700
CELL_SIZE = 8
FPS = 60

TOGGLE = 1
BRUSH_RADIUS = 2

def main():
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Physic Simulation - Lorenzo")
    clock = pygame.time.Clock()
    
    text_phrase = '1: SAND | 2: WATER | 3: DIRT | 4: REMOVE | UP/DOWN TO CHANGE THE BRUSH (0-4) | R: RESET'
    
    font = pygame.font.Font('freesansbold.ttf', 20)
    text = font.render(text_phrase,True, (255, 255, 0))
    textRect = text.get_rect()
    textRect.center = (WIDTH // 2, 50)
    
    global TOGGLE
    global BRUSH_RADIUS
    
    matrix = library.init_matrix(WIDTH, HEIGHT, CELL_SIZE)
    run = True
    
    while run:
        clock.tick(FPS)
    
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                run = False
            
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_r:
                    library.reset_matrix(matrix, WIDTH, HEIGHT, CELL_SIZE)
                
                if e.key == pygame.K_1:
                    TOGGLE = 1
                
                if e.key == pygame.K_2:
                    TOGGLE = 2
                    
                if e.key == pygame.K_3:
                    TOGGLE = 3
                    
                if e.key == pygame.K_4:
                    TOGGLE = 4
                    
                if e.key == pygame.K_UP:
                    if BRUSH_RADIUS < 4:
                        BRUSH_RADIUS += 1
                
                if e.key == pygame.K_DOWN:
                    if BRUSH_RADIUS > 0:
                        BRUSH_RADIUS -= 1
                    
            if pygame.mouse.get_pressed()[0]:
                mx, my = pygame.mouse.get_pos()
                library.draw_sand(matrix, (mx, my), CELL_SIZE, TOGGLE, BRUSH_RADIUS)
                    
        screen.fill((0, 0, 0))
    
        library.draw_matrix(screen, matrix, HEIGHT, WIDTH, CELL_SIZE)
        library.update_sand(matrix)
        
        screen.blit(text, textRect)
        
        pygame.display.flip()
    pygame.quit()
main()