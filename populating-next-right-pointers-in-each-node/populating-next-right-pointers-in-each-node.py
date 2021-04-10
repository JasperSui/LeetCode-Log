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
        if not root: return root
        next_level = deque([root])
        while next_level:
            curr_level = deque()
            n = None
            while next_level:
                curr = next_level.popleft()
                if curr.right: curr_level.append(curr.right)
                if curr.left: curr_level.append(curr.left)
                curr.next = n
                n = curr
            next_level = curr_level
        return root
            