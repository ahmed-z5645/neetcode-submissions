class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        ans = []

        for i in nums:
            count[i] = count.get(i, 0) + 1

        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])
        arr.sort()

        while len(ans) < k:
            ans.append(arr.pop()[1])
        
        return ans