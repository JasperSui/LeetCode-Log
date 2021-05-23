# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: TreeNode, val: int, depth: int) -> TreeNode:
        if not root: return TreeNode(val)
        self.d = defaultdict(list)
        def dfs(node, level, depth):
            if not node: return
            dfs(node.left, level+1, depth)
            self.d[level].append(node)
            dfs(node.right, level+1, depth)
        dfs(root, 1, depth)

        if depth == 1:
            t_left, t_right = root, None
            root = TreeNode(val)
            root.left, root.right = t_left, t_right
        else:
            for node in self.d[depth-1]:
                t_left, t_right = node.left, node.right
                node.left = TreeNode(val)
                node.right = TreeNode(val)
                node.left.left = t_left
                node.right.right = t_right
        return root