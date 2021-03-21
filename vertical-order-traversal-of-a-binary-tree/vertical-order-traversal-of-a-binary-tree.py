# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        # Time: O(NlogN)
        # Sapce: O(N)
        
        # # Iterative
        # x = y = 0
        # res = defaultdict(lambda: defaultdict(list))
        # queue = [(root, 0, 0)]
        # while queue:
        #     node, x, y = queue.pop(0)
        #     if node:
        #         res[x][y].append(node.val)
        #         queue.append((node.left, x-1, y+1))
        #         queue.append((node.right, x+1, y+1))
        # res = dict(sorted(res.items()))
        # res_2 = []
        # for x, d in res.items():
        #     tmp = []
        #     for y in d.keys():
        #         res[x][y].sort()
        #         tmp.extend(res[x][y])
        #     res_2.append(tmp)
        # return res_2
        
        # Recursive
        vals = []
        def preorder(node, x=0, y=0):
            if not node: return
            vals.append((x, y, node.val))
            preorder(node.left, x-1, y+1)
            preorder(node.right, x+1, y+1)
        preorder(root)
        ans = []
        last_x = -1000
        for x, y, v in sorted(vals):
            if x != last_x:
                ans.append([])
                last_x = x
            ans[-1].append(v)
        return ans
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        