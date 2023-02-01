class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        map = {}
        length = 0

        while head != None:
            map[length] = head
            head = head.next
            length += 1

        return map[length // 2]