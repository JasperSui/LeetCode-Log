# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        # Time: O(n)
        # Space: O(height)
        
        # Recursive
        if not root: return []
        d = defaultdict(list)
        def dfs(node, level):
            if not node: return
            d[level].append(node.val)
            dfs(node.left, level+1)
            dfs(node.right, level+1)
        dfs(root, 0)
        return list(d.values())[::-1]