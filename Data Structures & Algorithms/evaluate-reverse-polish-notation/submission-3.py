class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i not in ("+", "-", "*", "/"):
                stack.append(int(i))
            else:
                a = stack.pop()
                b = stack.pop()
                if i == "+":
                    stack.append(a+b)
                if i == "-":
                    stack.append(b-a)
                if i == "*":
                    stack.append(a*b)
                if i == "/":
                    ans = b / a
                    if ans >= 0:
                        stack.append(math.floor(ans))
                    else:
                        stack.append(math.ceil(ans))
        return(stack[0])
        