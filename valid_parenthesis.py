class Solution:
    def isValid(self, s: str) -> bool:
        opening = "({["
        closing = ")}]"

        stack = []
        for char in s:
            if char in opening:
                stack.append(char)
            elif char in closing:
                i = closing.index(char)
                if stack == []:
                    return False
                lastChar = stack.pop()
                if lastChar != opening[i]:
                    return False
            # print(stack)
        return stack == []

print(Solution().isValid("([]{})"))