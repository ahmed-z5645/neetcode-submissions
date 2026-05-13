class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        res = 0
        
        for i in range(n if (n > 0) else -1 * n):
            if i == 0:
                res = x
            else:
                res *= x
        
        if n > 0:
            return res
        else:
            return (1/res)