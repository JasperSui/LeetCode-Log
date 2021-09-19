# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.d = defaultdict(lambda: defaultdict(list))
        def dfs(node, x=0, y=0):
            if not node: return
            self.d[x][y].append(node.val)
            dfs(node.left, x-1, y+1)
            dfs(node.right, x+1, y+1)
        dfs(root)
        self.d = dict(sorted(self.d.items()))
        res = []
        for d in self.d.values():
            temp = []
            d = dict(sorted(d.items()))
            for l in d.values():
                temp.extend([*sorted(l)])
            res.append(temp)
        return res
        