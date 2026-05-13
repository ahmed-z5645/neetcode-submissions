class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # m x n matrix
        m = len(matrix)

        new = [[0] * m for _ in range(m)]

        for i in range(m):
            for j in range(m):
                new[j][m - 1 - i] = matrix[i][j]

        for i in range(m):
            for j in range(m):
                matrix[i][j] = new[i][j]
             