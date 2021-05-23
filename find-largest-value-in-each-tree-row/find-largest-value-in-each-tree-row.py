# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        self.d = defaultdict(lambda: float('-inf'))
        if not root: return []
        def dfs(node, level=1):
            if not node: return
            dfs(node.left, level+1)
            self.d[level] = max(self.d[level], node.val)
            dfs(node.right, level+1)
        dfs(root)
        res = []
        while 1:
            for i in range(1, 500000):
                if self.d.get(i) is not None: res.append(self.d[i])
                else: break
            break
        return res