# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: TreeNode, val: int, depth: int) -> TreeNode:
        def dfs(node, height=1):
            if not node: return
            if depth == 1:
                t = TreeNode(val)
                t.left = node
                return t
            if height == depth-1:
                temp_left, temp_right = node.left, node.right
                node.left, node.right = TreeNode(val), TreeNode(val)
                node.left.left, node.right.right = temp_left, temp_right
            dfs(node.left, height+1)
            dfs(node.right, height+1)
        depth_1_ans = dfs(root)
        if depth == 1:
            return depth_1_ans
        return root