class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0:
            return []
        
        t = l = 0
        b = len(matrix) - 1
        r = len(matrix[0]) - 1

        ans = []

        while (l <= r) and (t <= b):

            temp = l
            while temp < r + 1:
                ans.append(matrix[t][temp])
                temp += 1
            t += 1

            temp = t
            while temp < b + 1:
                ans.append(matrix[temp][r])
                temp += 1
            r -= 1

            if t <= b:
                temp = r
                while l <= temp:
                    ans.append(matrix[b][temp])
                    temp -= 1
                b -= 1

            if l <= r:
                temp = b
                while t <= temp:
                    ans.append(matrix[temp][l])
                    temp -= 1
                l += 1
            
        return ans


