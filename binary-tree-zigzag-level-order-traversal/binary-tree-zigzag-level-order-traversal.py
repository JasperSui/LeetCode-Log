# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.res = defaultdict(list)
        def dfs(node, depth=0):
            if not node: return
            self.res[depth].append(node.val)
            dfs(node.left, depth+1)
            dfs(node.right, depth+1)
        dfs(root)
        
        res = []
        for i, l in enumerate(list(self.res.values())):
            if i % 2 == 1:
                res.append(reversed(l))
            else:
                res.append(l)

        return res