# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        # Time: O(N)
        # Sapce: O(height)
        
        # Iterative
        x = y = 0
        res = defaultdict(lambda: defaultdict(list))
        queue = [(root, 0, 0)]
        while queue:
            node, x, y = queue.pop(0)
            if node:
                res[x][y].append(node.val)
                queue.append((node.left, x-1, y+1))
                queue.append((node.right, x+1, y+1))
        print(res)
        res = dict(sorted(res.items()))
        res_2 = []
        for x, d in res.items():
            tmp = []
            for y in d.keys():
                res[x][y].sort()
                tmp.extend(res[x][y])
            res_2.append(tmp)
        return res_2