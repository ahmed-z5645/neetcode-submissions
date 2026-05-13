class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = [False] * len(matrix), [False] * len(matrix[0])

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows[i] = True
                    cols[j] = True

        for i in range(len(rows)):
            if rows[i]:
                matrix[i] = [0] * len(matrix[i])

        for j in range(len(cols)):
            if cols[j]:
                for i in range(len(rows)):
                    matrix[i][j] = 0

        


        