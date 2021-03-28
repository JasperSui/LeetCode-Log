# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        if not root: return []
        res = []
        def dfs(node):
            if not node: return 0
            s = node.val + dfs(node.left) + dfs(node.right)
            res.append(s)
            return s
        dfs(root)
        c = Counter(res)
        max_sum, max_time = c.most_common(1)[0]
        return [s for s, t in c.items() if t == max_time]