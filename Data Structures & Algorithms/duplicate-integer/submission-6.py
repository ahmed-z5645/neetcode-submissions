class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for l in range(len(nums)):
                if i != l:
                    if nums[i] == nums[l]:
                        return True
        return False