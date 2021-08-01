# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        left = max_depth = ans = 0
        queue = deque([(root, 0, 0)])
        while queue:
            node, depth, pos = queue.popleft()
            if node:
                queue.append((node.left, depth+1, pos*2))
                queue.append((node.right, depth+1, pos*2+1))
                if max_depth != depth:
                    max_depth = depth
                    left = pos
                ans = max(ans, pos - left + 1)
        return ans