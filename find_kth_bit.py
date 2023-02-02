class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invert(binary: str):
            inverted = ""
            for item in binary:
                inverted += "0" if item == "1" else "1"
            return inverted

        def buildBinary(n: int):
            if n <= 1:
                return "0"
            else: 
                return buildBinary(n - 1) + "1" + invert(buildBinary(n - 1))[::-1]
        # print(buildBinary(n))
        return buildBinary(n)[k-1]