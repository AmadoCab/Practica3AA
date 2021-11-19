# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        one = head
        if one == None:
            return one
        two = head.next
        if two == None:
            return one
        one.next = None
        while two.next != None:
            zero, one, two = one, two, two.next
            one.next = zero
        zero, one = one, two
        one.next = zero
        return one

# EOF #
