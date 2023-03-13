class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        occur = {}
        stack = []
        visited = set()

        for index, value in enumerate(s):
            occur[value] = index

        for index, value in enumerate(s):
            if value not in visited:
                
                while stack and stack[-1] > value and occur[stack[-1]] > index:
                    visited.remove(stack.pop())

                stack.append(value)
                visited.add(value)

        return "".join(stack)
