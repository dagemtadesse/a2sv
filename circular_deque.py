class MyCircularDeque:

    def __init__(self, k: int):
        self.list = [None] * k 
        self.front = 0
        self.back = 0
        self.size = k
        self.count = 0

    def insertFront(self, value: int) -> bool:
        if self.list[self.front] is None:
            self.list[self.front] = value
            self.count += 1
            return True
        if not self.list[self.front] is None and not self.isFull():
            self.front = (self.front + 1) % self.size
            self.list[self.front] = value
            self.count += 1
            return True
        return False



    def insertLast(self, value: int) -> bool:
        if self.list[self.back] is None:
            self.list[self.back] = value
            self.count += 1
            return True
        if not self.list[self.back] is None and not self.isFull():
            self.back = (self.back - 1) % self.size
            self.list[self.back] = value
            self.count += 1
            return True
        return False
        

    def deleteFront(self) -> bool:
        if(self.list[self.front] is None):
            return False
        self.list[self.front] = None
        self.count -=1
        if not self.isEmpty():
            self.front = (self.front - 1) % self.size
        return True


    def deleteLast(self) -> bool:
        if(self.list[self.back] is None):
            return False
        self.list[self.back] = None
        self.count -=1
        if not self.isEmpty():
            self.back = (self.back + 1) % self.size
        return True


    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.list[self.front]


    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.list[self.back]


    def isEmpty(self) -> bool:
        return self.count == 0
        

    def isFull(self) -> bool:
        return self.count == self.size
   
        
d = MyCircularDeque(4)
d.insertFront(9)
d.deleteLast()
print(d.list)
print(d.front, d.back)