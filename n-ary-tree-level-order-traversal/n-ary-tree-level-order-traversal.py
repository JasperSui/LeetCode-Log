"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        self.d = defaultdict(list)
        def dfs(node, depth=1):
            if not node: return
            self.d[depth].append(node.val)
            for child in node.children:
                dfs(child, depth+1)
        dfs(root)
        return list(self.d.values())