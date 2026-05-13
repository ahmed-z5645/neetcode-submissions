class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        bigList = []
        hmap = defaultdict(list)
        
        for s in strs:
            bigList.append([0] * 26)
        
        for i in range(len(strs)):
            lower = strs[i].lower()

            for letter in lower:
                index = ord(letter)
                bigList[i][index - ord('a')] += 1

            hmap[tuple(bigList[i])].append(strs[i])

        ans = []

        for i in hmap.values():
            ans.append(i)

        return ans