# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
#     def __init__(self):
#         self.d = {}

#     def rob(self, root: TreeNode) -> int:
#         # Time: O(n)
#         # Space: O(height)
#         if not root: return 0
#         if root in self.d: return self.d[root]
#         ans = 0
#         if root.left:
#             ans += self.rob(root.left.left) + self.rob(root.left.right)
#         if root.right:
#             ans += self.rob(root.right.left) + self.rob(root.right.right)
#         ans = max(ans + root.val, self.rob(root.left) + self.rob(root.right))
#         self.d[root] = ans
#         return ans

    # Genius way
    def rob(self, root: TreeNode) -> int:
        return max(self.rob_sub(root))

    def rob_sub(self, root):
        if not root: return (0, 0)
        left_1, left_2 = self.rob_sub(root.left)
        right_1, right_2 = self.rob_sub(root.right)
        res = (max(left_1, left_2) + max(right_1, right_2), root.val + left_1 + right_1)
        return res