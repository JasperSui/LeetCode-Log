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
        self.d = defaultdict(list)
        def dfs(node, level=0):
            if not node: return
            self.d[level].append(node)
            dfs(node.left, level+1)
            dfs(node.right, level+1)
        dfs(root)
        for l in self.d.values():
            for i in range(len(l)):
                if i == len(l) - 1: l[i].next = None
                else:
                    l[i].next = l[i+1]
        return root
                