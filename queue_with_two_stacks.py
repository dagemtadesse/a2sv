class MyQueue:

    def __init__(self):
        self.input = []
        

    def push(self, x: int) -> None:
        self.input.append(x)

    def pop(self) -> int:
        output = []
        while self.input != []:
            output.append(self.input.pop())
        elem =  output.pop()
        while output != []:
            self.input.append(output.pop())
        return elem

    def peek(self) -> int:
        output = []
        while self.input != []:
            output.append(self.input.pop())
        elem =  output.pop()
        self.input.append(elem)
        while output != []:
            self.input.append(output.pop())
        return elem

    def empty(self) -> bool:
        # print(self.input)
        return len(self.input) == 0


q = MyQueue()
for i in range(5):
    q.push(i)
while not q.empty():
    # print(q.peek())
    print(q.pop())
    # q.pop()
    print("len", q.input)