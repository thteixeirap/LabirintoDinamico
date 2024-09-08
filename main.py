import pygame
import time
from config import WIDTH, HEIGHT, FPS, CELL_SIZE, OBSTACLE_CREATION_INTERVAL
from labirinto import Labirinto
from pacman import PacMan
from utils import draw_grid, draw_path, draw_text

# Inicialização do Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Labirinto Dinâmico com Três Pac-Mans")
clock = pygame.time.Clock()

# Configuração do labirinto
grid = [[0 for _ in range(50)] for _ in range(50)]
labirinto = Labirinto(grid)

# Configuração dos Pac-Mans
pacman_bfs = PacMan(labirinto, (0, 0), (49, 49), "bfs", (255, 255, 0))  # Amarelo para BFS
pacman_a_star = PacMan(labirinto, (0, 0), (49, 49), "a_star", (255, 0, 0))  # Vermelho para A*
pacman_dfs = PacMan(labirinto, (0, 0), (49, 49), "dfs", (0, 255, 0))  # Verde para DFS

pacmans = [pacman_bfs, pacman_a_star, pacman_dfs]

# Loop principal
running = True
last_obstacle_time = time.time()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Adiciona um novo obstáculo periodicamente
    if time.time() - last_obstacle_time > OBSTACLE_CREATION_INTERVAL:
        labirinto.add_new_obstacle()
        last_obstacle_time = time.time()

    # Atualiza os caminhos dos Pac-Mans
    for pacman in pacmans:
        pacman.move()

    # Desenha o labirinto e os Pac-Mans
    screen.fill((255, 255, 255))
    draw_grid(screen, labirinto, CELL_SIZE)
    for pacman in pacmans:
        path_color = (255, 255, 0) if pacman.algorithm == "bfs" else \
                     (255, 0, 0) if pacman.algorithm == "a_star" else \
                     (0, 255, 0)
        draw_path(screen, pacman.path, path_color, CELL_SIZE)
    draw_text(screen, f"Pac-Man BFS: {pacman_bfs.initial_path_length} / {pacman_bfs.actual_steps} passos, {pacman_bfs.recalculation_count} recalculos", 20, (255, 255, 0), (10, 10))
    draw_text(screen, f"Pac-Man A*: {pacman_a_star.initial_path_length} / {pacman_a_star.actual_steps} passos, {pacman_a_star.recalculation_count} recalculos", 20, (255, 0, 0), (10, 30))
    draw_text(screen, f"Pac-Man DFS: {pacman_dfs.initial_path_length} / {pacman_dfs.actual_steps} passos, {pacman_dfs.recalculation_count} recalculos", 20, (0, 255, 0), (10, 50))
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
