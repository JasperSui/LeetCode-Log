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
#         self.d = defaultdict(list)
#         def dfs(node, level=0):
#             if not node: return
#             self.d[level].append(node)
#             dfs(node.left, level+1)
#             dfs(node.right, level+1)
#         dfs(root)
#         for l in self.d.values():
#             for i in range(len(l)):
#                 if i == len(l) - 1: l[i].next = None
#                 else:
#                     l[i].next = l[i+1]
#         return root
        
        if not root: return
        curr = root
        p = dummy = Node()
        while curr:
            if curr.left:
                p.next = curr.left
                p = p.next
            if curr.right:
                p.next = curr.right
                p = p.next
            if curr.next:
                curr = curr.next
            else:
                curr = dummy.next
                dummy.next = None
                p = dummy
        return root