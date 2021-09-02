# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.res = []
        def dfs(node, path=[]):
            if not node: return
            new_path = path + [str(node.val)]
            if not node.left and not node.right:
                self.res.append("->".join(new_path))
            dfs(node.left, new_path)
            dfs(node.right, new_path)
        dfs(root)
        return self.res