"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: return []
        stack = [root]
        res = []
        while stack:
            new_stack = []
            temp = []
            for node in stack:
                temp.append(node.val)
                
                for child in node.children:
                    new_stack.append(child)
            res.append(temp)
            stack = new_stack
        return res
        