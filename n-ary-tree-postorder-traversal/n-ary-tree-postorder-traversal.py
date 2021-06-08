"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        self.res = []
        def dfs(node):
            if not node: return
            for c in node.children:
                dfs(c)
            self.res.append(node.val)
        dfs(root)
        return self.res
        
        
        
        
        
        
        
        
        
        
        
        
        # Time: O(N)
        # Space: O(height)
        
        # Iterable (using stack)
        res = []
        if not root: return res
        stack = [root]
        while stack:
            curr = stack.pop()
            res.append(curr.val)
            stack.extend(curr.children)
        return res[::-1] # Post Order
        
        # # Recursive
        # res = []
        # def dfs(node):
        #     if not node: return
        #     if node.children:
        #         for c in node.children:
        #             dfs(c)
        #     res.append(node.val)
        # dfs(root)
        # return res