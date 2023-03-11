class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {}
        stack = []

        operations['+'] = lambda x, y: x + y
        operations['-'] = lambda x, y: x - y
        operations['*'] = lambda x, y: x * y
        operations['/'] = lambda x, y: x / y

        for token in tokens:
            if not token in operations:
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()
                stack.append(int(operations[token](a, b)))
        return stack.pop()
