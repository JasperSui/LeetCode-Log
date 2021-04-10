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
        # Time: O(n)
        # Space: O(n)
        
        # Iterative
        # if not root: return root
        # next_level = deque([root])
        # while next_level:
        #     curr_level = deque()
        #     n = None
        #     while next_level:
        #         curr = next_level.popleft()
        #         if curr.right: curr_level.append(curr.right)
        #         if curr.left: curr_level.append(curr.left)
        #         curr.next = n
        #         n = curr
        #     next_level = curr_level
        # return root
        
        # Recursive
        if not root: return None
        self.connect_left_and_right(root.left, root.right)
        return root
    
    def connect_left_and_right(self, n1, n2):
        if not n1 or not n2: return None
        n1.next = n2
        self.connect_left_and_right(n1.left, n1.right)
        self.connect_left_and_right(n2.left, n2.right)
        self.connect_left_and_right(n1.right, n2.left)
            