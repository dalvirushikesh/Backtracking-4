# Time Complexity: O(C(h*w, n) * h * w) in the worst case
#   - C(h*w, n) = number of ways to place n buildings in h*w grid
#   - BFS runs in O(h * w) for each placement
# Space Complexity: O(h * w)
#   - For the grid, visited matrix, and BFS queue

from collections import deque
import sys

class Solution:
    def __init__(self):
        self.minDist = sys.maxsize

    def optimalBuildingPlacement(self, h: int, w: int, n: int) -> int:
        grid = [[-1 for _ in range(w)] for _ in range(h)]
        self.backtrack(grid, n, 0, 0)
        return self.minDist

    def backtrack(self, grid, n, row, col):
        if n == 0:
            self.minDist = min(self.minDist, self.bfs(grid))
            return
        for i in range(row, len(grid)):
            for j in range(col if i == row else 0, len(grid[0])):
                if grid[i][j] == -1:
                    grid[i][j] = 0
                    self.backtrack(grid, n - 1, i, j + 1)
                    grid[i][j] = -1

    def bfs(self, grid):
        h, w = len(grid), len(grid[0])
        visited = [[False for _ in range(w)] for _ in range(h)]
        q = deque()

        for i in range(h):
            for j in range(w):
                if grid[i][j] == 0:
                    q.append((i, j))
                    visited[i][j] = True

        dist = -1
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        while q:
            for _ in range(len(q)):
                x, y = q.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny]:
                        visited[nx][ny] = True
                        q.append((nx, ny))
            dist += 1
        return dist
