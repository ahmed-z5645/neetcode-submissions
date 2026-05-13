class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l = len(nums)

        res = [False for _ in range(l)]

        res[0] = True

        for i, num in enumerate(nums):
            if num != 0 and res[i]:
                j = 1
                
                while j < num + 1:
                    print(j)
                    if (j + i) > l - 1:
                        return True
                    else:
                        res[j + i] = True
                        j += 1

        print(res)
        return res[-1]
        '''
        if 

        [ True, True, True, True, True ]

        dc about zero dc about false

        if last index is true return true
        '''
