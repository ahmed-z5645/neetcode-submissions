class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False

        hm = {
            "}" : "{",
            ")" : "(",
            "]" : "["
        }

        stack = []

        for i in s:
            if i not in hm:
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                    
                if hm[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
        
        if len(stack) != 0:
            return False
        
        return True

            
            

