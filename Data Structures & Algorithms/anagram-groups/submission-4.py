class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ ord(c) - ord('a') ] += 1
            
            res[tuple(count)].append(s)

        ans = []
        for i in res.values():
            ans.append(i)

        return ans
