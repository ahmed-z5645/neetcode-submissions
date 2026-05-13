class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == "+":
                a = stack.pop()
                b = stack.pop()
                ans = a + b
                stack.append(ans)
            elif i == "-":
                a = stack.pop()
                b = stack.pop()
                ans = b - a
                stack.append(ans)
            elif i == "*":
                a = stack.pop()
                b = stack.pop()
                ans = a * b
                stack.append(ans)
            elif i == "/":
                a = stack.pop()
                b = stack.pop()
                ans = b / a
                if ans >=0:
                    ans = math.floor(ans)
                    stack.append(ans)
                else:
                    ans = math.ceil(ans)
                    stack.append(ans)
            else:
                stack.append(int(i))
        return(stack[0])
        