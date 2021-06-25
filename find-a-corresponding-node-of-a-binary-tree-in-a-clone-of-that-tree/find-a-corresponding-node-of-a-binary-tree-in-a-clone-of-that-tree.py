# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        self.count = 0
        self.target_count = float('-inf')
        self.ans = None
        def dfs(node, is_clone=False):
            if not node: return
            if node == target or self.count == self.target_count:
                if is_clone:
                    self.ans = node
                else:
                    self.target_count = self.count
            if node.left:
                self.count += 1
                dfs(node.left, is_clone)
            if node.right:
                self.count += 1
                dfs(node.right, is_clone)
        dfs(original)
        self.count = 0
        dfs(cloned, True)
        return self.ans