# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # BFS
        queue = deque([root])
        while queue:
            curr = queue.popleft()
            if curr:
                curr.left, curr.right = curr.right, curr.left
                queue.append(curr.left)
                queue.append(curr.right)
        return root
        
        # if root:
        #     root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        #     return root