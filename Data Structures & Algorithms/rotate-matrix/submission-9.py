class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        '''
        t - r
        r - b
        b - l
        l - t
        '''

        l = t = 0
        b = len(matrix) - 1
        r = len(matrix[0]) - 1

        while l < r and t < b:
            index = 0
            while index + l < r:
                temp = matrix[t + index][r]
                matrix[t + index][r] = matrix[t][l + index]

                temp2 = matrix[b][r - index]
                matrix[b][r - index] = temp

                temp = matrix[b - index][l]
                matrix[b - index][l] = temp2

                temp2 = matrix[t][l + index]
                matrix[t][l + index] = temp
                
                index += 1
            t += 1
            l += 1
            b -= 1
            r -= 1
        


