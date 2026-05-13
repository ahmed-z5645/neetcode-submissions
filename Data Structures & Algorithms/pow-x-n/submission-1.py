class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 0
        if n == 0:
            return 1

        if n > 0:
            absval = n
        else:
            absval = -1 * n
        for i in range(absval):
            if i == 0:
                res = x
            else:
                res *= x
        
        if n > 0:
            return res
        else:
            return (1/res)