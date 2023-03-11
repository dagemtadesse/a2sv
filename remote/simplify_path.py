class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        curDir = ""
        for index, char in enumerate(path[1:]):

            if char != '/' and (index == len(path) - 2):
                curDir += char
                char = '/'

            if char == '/':
                if curDir == '..':
                    if len(stack) > 0:
                        stack.pop()
                elif curDir == '.':
                    pass
                else:
                    if curDir != "":
                        stack.append(curDir)
                curDir = ""
            else:
                curDir += char

        return "/" + "/".join(stack)
