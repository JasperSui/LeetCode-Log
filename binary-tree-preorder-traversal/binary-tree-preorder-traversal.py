# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        self.res = []
        def dfs(node):
            if not node: return
            self.res.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return self.res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # Time: O(N)
        # Space: O(height)
        self.res = []
        def dfs(node):
            if not node: return
            self.res.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return self.res
        
        # # Recursive 1
        # return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right) if root else []
        
        # Recursive 2
        # res = []
        # def dfs(node):
        #     if node:
        #         res.append(node.val)
        #         dfs(node.left)
        #         dfs(node.right)
        # dfs(root)
        # return res
    
        # # Iterative
        # if not root: return []
        # res, stack = [], [root]
        # while stack:
        #     curr = stack.pop()
        #     res.append(curr.val)
        #     if curr.right: stack.append(curr.right)
        #     if curr.left: stack.append(curr.left)
            
        # return res
        
        
        
        def preorder(node):
            if node is None: return None
            print(node.val)
            inorder(node.left)
            inorder(node.right)

        preorder(root)
        
        
        