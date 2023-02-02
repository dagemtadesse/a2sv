# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr = []
        maxTwinSum = 0

        while head != None:
            arr.append(head.val)
            head = head.next
        
        for i in range(len(arr)//2):
            maxTwinSum = max(maxTwinSum, arr[i] + arr[len(arr) - i - 1])
        
        return maxTwinSum