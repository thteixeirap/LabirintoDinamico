import random

class Labirinto:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.new_obstacle_color = (0, 0, 255)
        self.fixed_obstacle_color = (0, 0, 0)
        self.create_initial_obstacles()
        self.discovered_obstacles = set()

    def create_initial_obstacles(self):
        num_fixed_obstacles = 800
        for _ in range(num_fixed_obstacles):
            self.create_obstacle(self.fixed_obstacle_color)

    def create_obstacle(self, color):
        while True:
            x, y = random.randint(0, self.rows - 1), random.randint(0, self.cols - 1)
            if self.grid[x][y] == 0 and (x, y) != (0, 0) and (x, y) != (self.rows - 1, self.cols - 1):
                self.grid[x][y] = 1 if color == self.fixed_obstacle_color else 2
                break

    def add_new_obstacle(self):
        while True:
            x, y = random.randint(0, self.rows - 1), random.randint(0, self.cols - 1)
            if self.grid[x][y] == 0 and (x, y) != (0, 0) and (x, y) != (self.rows - 1, self.cols - 1):
                self.create_obstacle(self.new_obstacle_color)
                break

    def neighbors(self, position):
        x, y = position
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.rows and 0 <= ny < self.cols and self.grid[nx][ny] == 0:
                yield (nx, ny)

    def is_valid_position(self, position, known_only=False):
        x, y = position
        if known_only:
            return (0 <= x < self.rows and 0 <= y < self.cols and 
                    (self.grid[x][y] == 0 or (x, y) in self.discovered_obstacles))
        return 0 <= x < self.rows and 0 <= y < self.cols and self.grid[x][y] == 0

    def discover_obstacle(self, position):
        if self.grid[position[0]][position[1]] == 2:
            self.discovered_obstacles.add(position)
            self.grid[position[0]][position[1]] = 1
