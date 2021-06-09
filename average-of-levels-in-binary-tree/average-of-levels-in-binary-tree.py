# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root):
        averages = []
        level = [root]
        while level:
            averages.append(sum(node.val for node in level) / len(level))
            level = [kid for node in level for kid in (node.left, node.right) if kid]
        return averages