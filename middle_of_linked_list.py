# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        left = head
        right = head

        length = 0
        index = 0

        while True:
            if right != None:
                right = right.next
                length += 1
            elif left != None and length // 2 != index:
                left = left.next
                index += 1
            else:
                break

        return left