# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        middle = head
        i = 1
        while head.next != None:
            head = head.next
            i += 1
            if i == 2:
                middle = middle.next
                i = 0
        return middle

# EOF #
