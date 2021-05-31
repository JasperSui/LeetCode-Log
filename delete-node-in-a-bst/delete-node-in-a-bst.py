# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root: return
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            temp = root.right
            min_v = temp.val
            while temp and temp.left:
                temp = temp.left
                min_v = temp.val
            root.val = min_v
            root.right = self.deleteNode(root.right, root.val)
        return root
        
        
        
        
        
        # if not root: return
        # if root.val > key: 
        #     root.left = self.deleteNode(root.left, key)
        # elif root.val < key:
        #     root.right = self.deleteNode(root.right, key)
        # else: # root.val == key
        #     if not root.left:
        #         return root.right
        #     if not root.right:
        #         return root.left
        #     # left and right are both not null
        #     temp = root.right
        #     min_v = temp.val
        #     while temp and temp.left: 
        #         temp = temp.left
        #         min_v = temp.val
        #     root.val = min_v
        #     root.right = self.deleteNode(root.right, root.val)
        # return root