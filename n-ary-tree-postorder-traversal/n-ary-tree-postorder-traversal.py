"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        def dfs(node):
            if not node: return
            if node.children:
                for c in node.children:
                    dfs(c)
            res.append(node.val)
        dfs(root)
        return res