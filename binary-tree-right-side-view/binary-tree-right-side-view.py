# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root: return []
        self.d = defaultdict(list)
        def dfs(node, level=0):
            if not node: return
            self.d[level].append(node.val)
            dfs(node.left, level+1)
            dfs(node.right, level+1)
        dfs(root)
        ans = [l[-1] for l in self.d.values()]
        return ans