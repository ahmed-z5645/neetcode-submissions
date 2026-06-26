class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        res = []

        for key in freq:
            res.append([freq[key], key])

        res.sort()

        j = 0

        ans = []

        while j < k:
            ans.append(res[len(res) - j - 1][1])
            j += 1

        return ans