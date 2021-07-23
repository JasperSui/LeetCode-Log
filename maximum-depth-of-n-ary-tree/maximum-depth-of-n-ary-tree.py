"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        self.depth = 0
        def dfs(node, depth=1):
            if not node: return
            self.depth = max(self.depth, depth)
            for child in node.children:
                dfs(child, depth+1)
        dfs(root)
        return self.depth