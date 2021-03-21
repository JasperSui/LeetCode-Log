# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        # Time: O(N)
        # Space: O(height)
        
        # # Iterative 1
        # d = defaultdict(int)
        # l = 0
        # stack = [(root, 0)]
        # while stack:
        #     node, level = stack.pop()
        #     if node:
        #         if not node.left and not node.right:
        #             d[level] += node.val
        #             l = max(l, level)
        #         stack.append((node.left, level+1))
        #         stack.append((node.right, level+1))
        # return d[l]
        
        # Iterative 2
        next_level = [root]
        while next_level:
            cur_level = next_level
            next_level = []
            for node in cur_level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
        return sum([node.val for node in cur_level])
        
        # # Recursive
        # d = defaultdict(int)
        # def preorder(node, level=0):
        #     if not node: return
        #     d[level] += node.val
        #     preorder(node.left, level+1)
        #     preorder(node.right, level+1)
        # preorder(root)
        # _, ans = d.popitem()
        # return ans