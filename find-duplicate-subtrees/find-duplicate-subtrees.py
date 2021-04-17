# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        treeid = defaultdict()
        trees = defaultdict(list)
        treeid.default_factory = treeid.__len__
        def getid(node):
            if not node: return
            id = treeid[node.val, getid(node.left), getid(node.right)]
            trees[id].append(node)
            return id
        getid(root)
        return [roots[0] for roots in trees.values() if roots[1:]]
            
    