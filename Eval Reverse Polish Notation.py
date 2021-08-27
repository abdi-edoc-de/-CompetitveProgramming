

class Solution:
    def evalRPN(self, tokens):
        op = "-+/*"
        stack = []

        for i in tokens:
            if i not in op:
                if '-' in i:
                    stack.append(f'({i})')
                else:
                    stack.append(i)

            elif i in op:
                right = (stack.pop())
                left = (stack.pop())
                val = int(eval(f'{left}{i}{right}'))
                stack.append(f"{val}")
        return int(stack.pop())
            
obj = Solution()
print(obj.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))