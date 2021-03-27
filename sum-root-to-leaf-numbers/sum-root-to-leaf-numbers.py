# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        # Time: O(n)
        # Space: O(height)
        
        # # DFS
        # res = []
        # def dfs(node, l):
        #     if not node: return
        #     l = [*l, str(node.val)]
        #     if not node.left and not node.right: res.append(l)
        #     dfs(node.left, l)
        #     dfs(node.right, l)
        # dfs(root, [])
        # return sum(map(lambda x: int(''.join(x)), res))
        
        # Iterative
        stack = [(root, [])]
        res = []
        while stack:
            curr, l = stack.pop()
            if curr:
                l = [*l, str(curr.val)]
                if not curr.left and not curr.right: res.append(l)
                else:
                    stack.append((curr.left, l))
                    stack.append((curr.right, l))
        return sum(map(lambda x: int(''.join(x)), res))