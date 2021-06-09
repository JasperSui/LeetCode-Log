# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: TreeNode, val: int, depth: int) -> TreeNode:
        self.d = defaultdict(list)
        def dfs(node, level=1):
            if not node: return
            dfs(node.left, level+1)
            self.d[level].append(node)
            dfs(node.right, level+1)
        dfs(root)
        
        if depth == 1:
            node = TreeNode(val)
            node.left = root
            return node
        else:
            original_nodes = self.d[depth-1]
            for n in original_nodes:
                temp_left, temp_right = n.left, n.right
                n.left, n.right = TreeNode(val), TreeNode(val)
                n.left.left, n.right.right= temp_left, temp_right
            return root