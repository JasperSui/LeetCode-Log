# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        level = 1
        next_level = [root]
        res = []
        while next_level:
            curr_level = []
            temp = []
            while next_level:
                curr = next_level.pop()
                if curr:
                    temp.append(curr.val)
                    if level % 2 == 0:
                        if curr.right: curr_level.append(curr.right)
                        if curr.left: curr_level.append(curr.left)
                    else:
                        if curr.left: curr_level.append(curr.left)
                        if curr.right: curr_level.append(curr.right)
            res.append(temp)
            next_level = curr_level
            level += 1
        return res