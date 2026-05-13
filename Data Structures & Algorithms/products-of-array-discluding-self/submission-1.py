class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        zeros = 0
        if len(nums) == 0:
            return []

        product = 1
        for i in range(len(nums)):
            if nums[i] != 0:
                product *= nums[i]
            else:
                zeros += 1

        if zeros >= 2:
            return [0] * len(nums)

        ans = []

        if zeros == 1:
            for i in range(len(nums)):
                if nums[i] == 0:
                    ans.append(int(product))
                else:
                    ans.append(0)
            
            return ans
        
        else:
            for i in nums:
                ans.append(int(product / i))
            return ans
            
        