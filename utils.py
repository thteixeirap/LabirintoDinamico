import pygame

def draw_grid(screen, labirinto, cell_size):
    for row in range(labirinto.rows):
        for col in range(labirinto.cols):
            color = (255, 255, 255)
            if labirinto.grid[row][col] == 1:
                color = labirinto.fixed_obstacle_color
            elif labirinto.grid[row][col] == 2:
                color = labirinto.new_obstacle_color
            pygame.draw.rect(screen, color, (col * cell_size, row * cell_size, cell_size, cell_size))

def draw_path(screen, path, color, cell_size):
    for (x, y) in path:
        pygame.draw.rect(screen, color, (y * cell_size, x * cell_size, cell_size, cell_size))

def draw_text(screen, text, size, color, position):
    font = pygame.font.SysFont(None, size)
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, position)
