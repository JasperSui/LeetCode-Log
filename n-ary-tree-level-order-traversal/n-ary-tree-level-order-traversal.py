"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        # Time: O(N)
        # Space: O(height)
        
        # Iterative 1
        res = defaultdict(list)
        def bfs(node, level=0):
            if node:
                res[level].append(node.val)
                for c in node.children:
                    bfs(c, level+1)
        bfs(root)
        return list(res.values())
            
        
            