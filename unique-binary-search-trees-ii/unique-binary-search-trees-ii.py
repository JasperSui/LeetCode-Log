# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        return self.generate(1, n)
    
    def generate(self, start, end):
        res = []
        if start > end:
            res.append(None)
        for i in range(start, end+1):
            left_list = self.generate(start, i-1)
            right_list = self.generate(i+1, end)
            for left in left_list:
                for right in right_list:
                    root = TreeNode(i)
                    root.left = left
                    root.right = right
                    res.append(root)
        return res
            