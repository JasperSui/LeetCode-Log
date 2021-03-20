"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        # Time: O(N)
        # Space: O(height)
        
        # # Iterable
        # res = []
        # if not root: return res
        # stack = [root]
        # while stack:
        #     curr = stack.pop()
        #     res.append(curr.val)
        #     stack.extend(curr.children[::-1] if curr.children else [])
        # return res
        
        # # Recrusive
        
        res = []
        def dfs(node):
            if not node: return
            res.append(node.val)
            if node.children:
                for c in node.children:
                    dfs(c)
        dfs(root)
        return res