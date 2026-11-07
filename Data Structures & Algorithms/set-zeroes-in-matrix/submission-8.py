class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = [False] * len(matrix), [False] * len(matrix[0])

        rows = []
        cols = []

        h = len(matrix)
        w = len(matrix[0])

        for row in range(h):
            for col in range(w):
                if matrix[row][col] == 0:
                    rows.append(row)
                    cols.append(col)

        for row in rows:
            matrix[row] = [0] * w

        for col in cols:
            for i in range(h):
                matrix[i][col] = 0
            