# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        d = defaultdict(int)
        self.curr_max = float('-inf')
        def dfs(node):
            if not node: return
            d[node.val] += 1
            self.curr_max = max(self.curr_max, d[node.val])
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return [k for k, v in d.items() if v == self.curr_max] if self.curr_max != float('-inf') else []