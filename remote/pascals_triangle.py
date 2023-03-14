class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex <= 0:
            return [1]
        else:
            prev = self.getRow(rowIndex - 1)
            print(prev)

            if len(prev) > 1:
                new = []
                for i in range(0, len(prev) - 1):
                    new.append(prev[i] + prev[i + 1])
                # print("-- new", new, "-- prev", prev)
                prev[1:-1] = new
            else:
                prev.append(1)
                
            return prev



