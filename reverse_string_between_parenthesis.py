class Solution:
    def reverseParentheses(self, s: str) -> str:
        # stacks = []
        # unmoved = {}
        # parentthesis = 0
        # depth = 0
        # result = ""

        # for index, char in enumerate(s):
        #     if char == "(":
        #         depth += 1
        #         parentthesis += 1
        #     elif char == ")":
        #         depth -= 1
        #         parentthesis += 1
        #     else:
        #         if depth == 0:
        #             unmoved[index - parentthesis] = char
        #         else:
        #             stacks.append(char)
        # print(stacks, unmoved)
        # for i in range(len(stacks) + len(unmoved)):
        #     if i in unmoved:
        #         result += unmoved[i]
        #     elif stacks != []:
        #         result += stacks.pop()

        # return result 
        temp = ""
        stack = []
        for char in s:
            if char == "(":
                stack.append(temp)
                temp = ""
            elif char == ")":
                reversed = ""
                for i in range(len(temp)- 1, -1, -1):
                    reversed += temp[i]
                temp = stack.pop() + reversed
            else:
                temp += char
        print(temp)


print(Solution().reverseParentheses('a(bcdefghijkl(mno)p)q'))
# print(Solution().reverseParentheses('(abcd)'))