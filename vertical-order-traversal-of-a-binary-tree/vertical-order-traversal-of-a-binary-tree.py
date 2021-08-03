# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        self.d = defaultdict(lambda: defaultdict(list))
        def dfs(node, x=0, depth=0):
            if not node: return
            self.d[x][depth].append(node.val)
            dfs(node.left, x-1, depth+1)
            dfs(node.right, x+1, depth+1)
        dfs(root)
        self.d = dict(sorted(self.d.items()))
        res = []
        for d in self.d.values():
            d = dict(sorted(d.items()))
            temp = []
            for l in d.values():
                l.sort()
                temp.extend([*l])
            res.append(temp)
        return res