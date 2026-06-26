class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []
        l = top = 0
        r = len(matrix[0]) - 1
        down = len(matrix) - 1
        ans = []
        while l <= r and top <= down:
            for i in range(l, r + 1):
                ans.append(matrix[top][i])
            top += 1

            for i in range(top, down + 1):
                ans.append(matrix[i][r])
            r -= 1

            if top <= down:
                for i in range(r, l - 1, -1):
                    ans.append(matrix[down][i])
                down -= 1

            if l <= r:
                for i in range(down, top - 1, -1):
                    ans.append(matrix[i][l])
                l += 1

        return ans