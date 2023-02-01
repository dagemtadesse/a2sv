# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        counter = {}

        top = head
        prev = ListNode(0, head)
 
        while not head is None:
            if head.val in counter:
                prev.next = head.next
                head = head.next
            else:
                counter[head.val] = True
                head = head.next
                prev = prev.next
        
        return top
