class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0

        islands = 0
        visited = set()
        rows, cols = len(grid), len(grid[0])

        def bfs(i, j):
            q = collections.deque()

            visited.add((i, j))
            q.append((i, j))

            directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    r, c = dr + row, dc + col

                    if (r in range(rows) and
                        c in range(cols) and
                        grid[r][c] == "1" and
                        ((r, c) not in visited)):
                        visited.add((r, c))
                        q.append((r, c))
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i, j) not in visited:
                    bfs(i, j)
                    islands += 1

        return islands

