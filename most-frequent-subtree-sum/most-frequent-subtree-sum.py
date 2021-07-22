# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        self.l = []
        def dfs(node):
            if not node: return 0
            l = dfs(node.left)
            r = dfs(node.right)
            s = node.val + l + r
            self.l.append(s)
            return s
        dfs(root)
        d = Counter(self.l)
        max_freq = max(d.values())
        
        return [k for k, v in d.items() if v == max_freq] if root else []