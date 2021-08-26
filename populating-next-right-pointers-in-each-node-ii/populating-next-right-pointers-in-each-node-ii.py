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
        queue = [root]
        while queue:
            new_queue = []
            queue.append(None)
            for i in range(len(queue)-1):
                queue[i].next = queue[i+1]
            queue.pop()
            
            for node in queue:
                if node:
                    if node.left:
                        new_queue.append(node.left)
                    if node.right:
                        new_queue.append(node.right)
            queue = new_queue
        return root