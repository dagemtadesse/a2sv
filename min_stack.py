class Node :
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
        
        self.min = min(self.val, self.next.min if not self.next is None else float('inf'))
    def __repr__(self) -> str:
        return "[ val: " + str(self.val) + " min: " + str(self.min) + (self.next.__repr__() if not self.next is None else "") + "]"

class MinStack:

    def __init__(self):
        self._head = None

    def push(self, val: int) -> None:
        new_head = Node(val, self._head)
        self._head = new_head

    def pop(self) -> None:
        self._head = self._head.next

    def top(self) -> int:
        return self._head.val

    def getMin(self) -> int:
        return self._head.min
        


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
for i in [-2, 0, -1]:
    obj.push(i)
    print(obj._head, "end", i)
    # print(obj.getMin())
# print("---")
# print(obj.getMin())
# print(obj.top())
# print(obj.pop())
# print(obj.getMin())

# print("---")
