# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        self.res = []
        def dfs(node, path=""):
            if not node: return
            new_path = path+str(node.val)
            dfs(node.left, new_path)
            dfs(node.right, new_path)
            if not node.left and not node.right: self.res.append(new_path)
        dfs(root)
        return sum([int(path, 2) for path in self.res])
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         self.ans = 0
        
#         def calc(root, path):
            
#             if root.left:
#                 calc(root.left, path + str(root.val))
            
#             if root.right:
#                 calc(root.right, path + str(root.val))
            
#             if not root.left and not root.right:
#                 path += str(root.val)
#                 self.ans += int(path, 2)
            
#         calc(root, "")
#         return self.ans
        result = 0
        stack = [[root, ""]]
        
        while stack:
            
            curr, path = stack.pop(0)
            if curr.left:
                stack.append([curr.left, path + str(curr.val)])
            if curr.right:
                stack.append([curr.right, path + str(curr.val)])
            if not curr.left and not curr.right:
                path += str(curr.val)
                result += int(path, 2)
                
        return result