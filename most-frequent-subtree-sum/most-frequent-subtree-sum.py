# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        if not root: return []
        self.d = []
        def dfs(node):
            if not node: return 0
            l = dfs(node.left)
            r = dfs(node.right)
            s = node.val + l + r
            self.d.append(s)
            return s
        dfs(root)
        counter = collections.Counter(self.d).most_common()
        return [a for a, b in counter if b == counter[0][1]]