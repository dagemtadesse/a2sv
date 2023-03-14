class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def reverse(s, start, end):
            if end - start < 1 :
                return
            s[start], s[end] = s[end], s[start]
            reverse(s, start+1, end-1)
        
        reverse(s, 0, len(s) -1)
