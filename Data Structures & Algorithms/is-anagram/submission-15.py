class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t): return False

        hmap1 = {}
        hmap2 = {}

        for i in range(len(s)):
            if s[i] in hmap1:
                hmap1[s[i]] += 1
            else:
                hmap1[s[i]] = 1

            if t[i] in hmap2:
                hmap2[t[i]] += 1
            else:
                hmap2[t[i]] = 1

        if hmap1 == hmap2:
            return True
        else: return False