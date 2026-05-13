class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for i in range(len(nums)):
            if nums[i] in freq:
                freq[nums[i]] += 1
            else:
                freq[nums[i]] = 1

        res = []
        for key in freq:
            res.append([freq[key], key])

        res.sort()

        ans = []

        j = 0   

        while j < k:
            ans.append(res[len(res) - 1 - j][1])
            j += 1

        return ans






