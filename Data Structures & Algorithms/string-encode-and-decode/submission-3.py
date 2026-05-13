class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        res = ""

        for s in strs:
            res += str(len(s))
            res += "#"
            res += str(s)
        
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        
        if s == "0#":
            return [""]
        
        res = []

        i = 0
        while i < len(s):
            length = ""
            while s[i] != "#":
                length += str(s[i])
                i += 1
            length = int(length)

            old = i
            word = ""
            while i < old + length + 1:
                if i == old:
                    pass
                else:
                    word += s[i]
                i += 1
            res.append(word)
            print(word)
        
        return res