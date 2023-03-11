class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []

        for char in s:
            if char == '(':
                stack.append(char)
            else:
                last = stack.pop()
                if last == '(':
                    stack.append(1)
                else:
                    print(stack)
                    stack.append(int(last))
                    total = 0
                    while stack:
                        val = stack.pop()
                        if val == '(':
                            break
                        total += val
                    stack.append(total * 2)

        return sum(stack)
