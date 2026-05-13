class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        countMap = {}
        for i, num in enumerate(nums):
            countMap[target - num] = (i)

        for i, num in enumerate(nums):
            if num in countMap:
                if i != (countMap[num]):
                    return ([i, countMap[num]]);
        