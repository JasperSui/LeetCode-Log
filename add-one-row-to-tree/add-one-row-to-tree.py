# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if not root: return TreeNode(val)
        if depth == 1:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root
        
        def dfs(node, curr_depth=1):
            if not node: return
            if curr_depth + 1 == depth:
                temp_left, temp_right = node.left, node.right
                node.left, node.right = TreeNode(val), TreeNode(val)
                node.left.left, node.right.right = temp_left, temp_right
                return
            dfs(node.left, curr_depth+1)
            dfs(node.right, curr_depth+1)
        dfs(root)
        return root
                
        