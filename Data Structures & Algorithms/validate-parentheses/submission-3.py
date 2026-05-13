class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        half = len(s)
        if s[-1] in ('[', '{', '('):
            return False
        if s[0] in ('}', ']', ')'):
            return False
        if half % 2 != 0:
            return False
        
        for i in s:
            if i in ('(', '{', '['):
                stack.append(i)
            
            elif i == ']' and stack[-1] != '[':
                return False
            
            elif i == ')' and stack[-1] != '(':
                return False
            
            elif i == '}' and stack[-1] != '{':
                return False
                
            else:
                stack.pop()
        
        if len(stack) == 0:
            return True
        else:
            return False

