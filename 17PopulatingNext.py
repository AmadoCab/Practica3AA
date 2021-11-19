"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        def set_next(i,level):
            if i == (2**level)-2:
                queue[i].next = None
                return level+1
            queue[i].next = queue[i+1]
            return level
        if not root:
            return root
        queue = [root]
        i = 0
        level = 1
        while i < len(queue):
            if queue[i].left:
                queue.append(queue[i].left)
                queue.append(queue[i].right)
            level = set_next(i,level)
            i += 1
        return root

# EOF #
