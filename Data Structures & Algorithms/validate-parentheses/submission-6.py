class Solution:
    def isValid(self, s: str) -> bool:
        if (len(s) % 2) != 0:
            return False
        stack = []
        for i in s:
            if len(stack) != 0:
                if i =="}" and stack[len(stack) - 1] != "{":
                    return False
                elif i ==")" and stack[len(stack) - 1] != "(":
                    return False
                elif i =="]" and stack[len(stack) - 1] != "[":
                    return False
                elif i in ["(", "[", "{"]:
                    stack.append(i)
                else:
                    stack.pop(len(stack) - 1)
            else:
                if i in ["}", "]", ")"]:
                    return False
                else:
                    stack.append(i)

        if len(stack) == 0:
            return True
        else:
            return False
            
            

