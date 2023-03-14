class Solution:
    def decodeString(self, s: str) -> str:
#         print(s)
        size = ""

        depth = 0

        start, end = 0, 0
        prev = False

        for index, char in enumerate(s):
            if char.isdigit() and not prev:
                size += char
            elif char.isdigit() and depth == 0:
                return self.decodeString(s[:index]) + self.decodeString(s[index:])
            else:
                if char == '[':
                    start = index if depth == 0 else start
                    depth += 1
                if char == ']':
                    depth -= 1
                    if depth == 0:
                        end = index
                        break
                else:
                    prev = True

        if start == end and end == 0:
            return s

        result =  int(size) * self.decodeString(s[start + 1: end])
        result += self.decodeString(s[end + 1:])

        return result
