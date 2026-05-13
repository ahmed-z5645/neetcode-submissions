class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        res = []
        for i in nums:
            freq[i] = 1 + freq.get(i, 0)

        arr = []

        for i, cnt in freq.items():
            arr.append([cnt, i])

        arr.sort()

        while len(res) < k:
            res.append(arr.pop()[1])

        return res