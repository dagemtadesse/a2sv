# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left = ListNode(0, head)
        top = left

        length = 0
        leftLength = 0

        while head != None or left != None:
            if head != None:
                length += 1
                head = head.next
            else:
                if leftLength == (length - n):
                    break
                left = left.next
                leftLength += 1
        left.next = left.next.next
        return top.next
                

        