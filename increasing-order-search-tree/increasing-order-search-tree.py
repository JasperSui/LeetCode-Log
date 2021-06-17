# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode, tail=None) -> TreeNode:
        if not root: return tail
        res = self.increasingBST(root.left, root)
        root.left = None
        root.right = self.increasingBST(root.right, tail)
        return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        if not root: return tail
        res = self.increasingBST(root.left, root)
        print(res)
        print(root)
        root.left = None
        root.right = self.increasingBST(root.right, tail)
        return res
    
#     def __init__(self):
#         self.head, self.prev = None, None
#     def increasingBST(self, root: TreeNode) -> TreeNode:
#         if not root: return
#         self.increasingBST(root.left)
#         if self.prev:
#             root.left = None
#             self.prev.right = root
#         if not self.head:
#             self.head = root
#         self.prev = root
#         self.increasingBST(root.right)
#         return self.head
        