import pygame
import library

WIDTH, HEIGHT = 1200, 700
CELL_SIZE = 8
FPS = 60

TOGGLE = False

def main():
    global TOGGLE
    pygame.init()
    matrix = library.init_matrix(WIDTH, HEIGHT, CELL_SIZE)
    
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    run = True
    
    while run:
        clock.tick(FPS)
        
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                run = False
            
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:
                    TOGGLE = not TOGGLE
                
            if pygame.mouse.get_pressed()[0]:
                mx, my = pygame.mouse.get_pos()
                c = library.init_color(TOGGLE)
                library.draw_sand(matrix, (mx, my), CELL_SIZE, c)
                    
        screen.fill((0, 0, 0))
    
        library.draw_matrix(screen, matrix, HEIGHT, WIDTH, CELL_SIZE)
        library.update_sand(matrix)
        
        pygame.display.flip()
    pygame.quit()
main()