# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        self.target_index = 0
        self.curr_index = 0
        def dfs(node):
            if not node: return
            self.curr_index += 1
            if node == target:
                self.target_index = self.curr_index
            dfs(node.left)
            dfs(node.right)
        dfs(original)

        self.curr_index = 0
        self.res = None
        def dfs2(node):
            if not node: return
            self.curr_index += 1
            if self.curr_index == self.target_index:
                self.res = node
            dfs2(node.left)
            dfs2(node.right)
        dfs2(cloned)
        return self.res
            