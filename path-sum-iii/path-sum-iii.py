# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        self.res = 0
        d = defaultdict(int)
        d[0] = 1
        self.dfs(root, targetSum, 0, d)
        return self.res
    
    def dfs(self, node, target, curr, d):
        if not node: return
        curr += node.val
        old = curr - target
        
        self.res += d[old]
        d[curr] += 1
        
        self.dfs(node.left, target, curr, d)
        self.dfs(node.right, target, curr, d)
        
        d[curr] -= 1