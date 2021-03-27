# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        # Time: O(n)
        # Space: O(height)
        
        # DFS
        res = []
        def dfs(node, s, l):
            if not node: return
            s += node.val
            l1 = [*l, node.val]
            l2 = [*l, node.val]
            if not node.left and not node.right and s == targetSum: res.append(l1)
            if node.left: dfs(node.left, s, l1)
            if node.right: dfs(node.right, s, l2)
        dfs(root, 0, [])
        return res
            