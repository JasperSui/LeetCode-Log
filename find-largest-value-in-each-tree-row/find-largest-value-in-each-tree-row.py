# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        
        # BFS
        res = []
        levels = [root]
        while any(levels):
            res.append(max(node.val for node in levels))
            levels = [kid for node in levels for kid in (node.left, node.right) if kid]
        return res
            
            
        # DFS (a little stupid)
        # if not root: return []
        # self.level = 0
        # self.d = defaultdict(lambda: float('-inf'))
        # def dfs(node, level=1):
        #     if not node: return
        #     dfs(node.left, level+1)
        #     self.d[level] = max(self.d[level], node.val)
        #     dfs(node.right, level+1)
        #     self.level = level+1
        # dfs(root)
        # max_key = max(self.d.keys())
        # return [self.d[i] for i in range(1, max_key+1)]