class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        countMap = {}
        for i, num in enumerate(nums):
            if target - num in countMap:
                return [countMap[target - num], i]
            elif num not in countMap:
                countMap[num] = i