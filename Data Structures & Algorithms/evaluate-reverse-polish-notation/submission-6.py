class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = set()

        s.add('+')
        s.add('-')
        s.add('*')
        s.add('/')

        stack = []

        for i in tokens:
            if i not in s:
                stack.append(int(i))
            else:
                if i == '+':
                    ans = stack.pop() + stack.pop()
                    stack.append(ans)
                elif i == "-":
                    ans = -1 * (stack.pop() - stack.pop())
                    stack.append(ans)
                elif i == "*":
                    ans = stack.pop() * stack.pop()
                    stack.append(ans)
                else:
                    num1 = stack.pop()
                    num2 = stack.pop()

                    if num1 * num2 < 0 and num2 % num1 != 0:
                        stack.append((num2 // num1) + 1)
                    
                    else:
                        stack.append(num2 // num1)
        
        return stack[0]
