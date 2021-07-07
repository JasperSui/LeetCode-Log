# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        self.res = defaultdict(list)
        def dfs(node, level=0):
            if not node: return
            self.res[level].append(node.val)
            dfs(node.left, level+1)
            dfs(node.right, level+1)
        dfs(root)
        res = []
        for i in range(len(self.res)):
            temp = self.res[i]
            if i % 2 == 1:
                temp.reverse()
            res.append(temp)
        return res
            