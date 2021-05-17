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
        self.res = defaultdict(list)
        def traverse(node, level=0):
            if not node: return
            traverse(node.left, level+1)
            self.res[level].append(node)
            traverse(node.right, level+1)
        traverse(root)
        for level_list in self.res.values():
            for i in range(len(level_list)):
                if i == len(level_list) - 1:
                    level_list[i].next = None
                else:
                    level_list[i].next = level_list[i+1]
        return root