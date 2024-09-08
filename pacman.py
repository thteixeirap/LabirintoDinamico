from collections import deque

class PacMan:
    def __init__(self, labirinto, start, goal, algorithm, color):
        self.labirinto = labirinto
        self.position = start
        self.goal = goal
        self.algorithm = algorithm
        self.color = color
        self.initial_path = self.calculate_path()
        self.initial_path_length = len(self.initial_path)
        self.path = self.initial_path[:]
        self.actual_steps = 0
        self.recalculation_count = 0

    def calculate_path(self):
        if self.algorithm == "bfs":
            return self.bfs(self.position, self.goal)
        elif self.algorithm == "a_star":
            return self.a_star(self.position, self.goal)
        elif self.algorithm == "dfs":
            return self.dfs(self.position, self.goal)
        return []

    def bfs(self, start, goal):
        queue = deque([start])
        came_from = {start: None}
        
        while queue:
            current = queue.popleft()

            if current == goal:
                path = []
                while current is not None:
                    path.append(current)
                    current = came_from[current]
                path.reverse()
                return path

            for neighbor in self.labirinto.neighbors(current):
                if neighbor not in came_from:
                    queue.append(neighbor)
                    came_from[neighbor] = current

        return []

    def a_star(self, start, goal):
        open_set = [start]
        came_from = {}
        g_score = {start: 0}
        f_score = {start: self.heuristic(start, goal)}

        while open_set:
            current = min(open_set, key=lambda x: f_score.get(x, float('inf')))
            if current == goal:
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                path.reverse()
                return path

            open_set.remove(current)

            for neighbor in self.labirinto.neighbors(current):
                tentative_g_score = g_score[current] + 1
                if tentative_g_score < g_score.get(neighbor, float('inf')):
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + self.heuristic(neighbor, goal)
                    if neighbor not in open_set:
                        open_set.append(neighbor)

        return []

    def dfs(self, start, goal):
        stack = [start]
        came_from = {start: None}

        while stack:
            current = stack.pop()

            if current == goal:
                path = []
                while current is not None:
                    path.append(current)
                    current = came_from[current]
                path.reverse()
                return path

            for neighbor in self.labirinto.neighbors(current):
                if neighbor not in came_from:
                    stack.append(neighbor)
                    came_from[neighbor] = current

        return []

    def heuristic(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def update_path(self):
        self.path = self.calculate_path()
        self.recalculation_count += 1
        print(f"Recalculando o caminho do Pac-Man... Total de recalculos: {self.recalculation_count}")

    def move(self):
        if not self.path:
            return

        next_position = self.path[0]
        x, y = next_position

        if self.labirinto.grid[x][y] == 2:
            self.labirinto.discover_obstacle((x, y))
            self.update_path()
        else:
            self.position = next_position
            self.path.pop(0)
            self.actual_steps += 1
