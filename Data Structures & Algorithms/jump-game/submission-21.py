class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l = len(nums)
        if l == 1:
            return True

        helper = [False] * l
        helper[0] = True

        for i in range(l):
            if helper[i] == True:
                for j in range(nums[i]):
                    if i + j + 2 > l:
                        return True
                    else:
                        print(i + j + 1)
                        print(l)
                        helper[i + j + 1] = True

        return helper[-1]