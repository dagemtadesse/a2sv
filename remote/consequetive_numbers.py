class DataStream:

    def __init__(self, value: int, k: int):
        self._stream = []
        self._value = value
        self._k = k
        self.prevResult = False

    def consec(self, num: int) -> bool:
        self._stream.append(num)

        if self.prevResult:
            if num == self._value:
                return True
            else:
                self.prevResult = False
                return False
        
        if len(self._stream) <  self._k:
            return False
        else:
            count = self._k
            index = len(self._stream) - 1
            while count > 0:
                if self._value != self._stream[index]:
                    return False
                count -= 1
                index -= 1
            self.prevResult = True
            return True
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)
