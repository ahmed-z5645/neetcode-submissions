class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)
        dp[0] = True

        for i in range(len(nums)):
            if dp[i] == True:
                for j in range(nums[i]):
                    if (i + j + 1 <= len(dp) - 1):
                        
                        dp[i + j + 1] = True
                
            #if i == 0:
            #    return dp
            if dp[-1] == True:
                return True

        return False
            
