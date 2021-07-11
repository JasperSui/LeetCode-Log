# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def canMerge(self, trees: List[TreeNode]) -> TreeNode:
        nodes = {}
        indeg = defaultdict(int)
        for t in trees:
            if t.val not in indeg:
                indeg[t.val] = 0
            if t.left:
                indeg[t.left.val] += 1
                if t.left.val not in nodes: nodes[t.left.val] = t.left
            if t.right:
                indeg[t.right.val] += 1
                if t.right.val not in nodes: nodes[t.right.val] = t.right
            nodes[t.val] = t
        source = [k for k, v in indeg.items() if v == 0]
        if len(source) != 1: return
        
        visited = set()
        self.prev = float('-inf')
        self.is_valid = True
        
        def inorder(val):
            if val in visited:
                self.is_valid = False
                return
            visited.add(val)
            node = nodes[val]
            if node.left:
                node.left = inorder(node.left.val)
            if self.prev >= val:
                self.is_valid = False
                return
            self.prev = val
            if node.right:
                node.right = inorder(node.right.val)
            return node
        root = inorder(source[0])
        if len(visited) != len(nodes) or not self.is_valid:
            return
        return root
        
        
#         if len(trees) == 1:
#             if self.is_valid(trees[0]):
#                 return trees[0]
#             else:
#                 return None
#         d = {}
#         for root in trees:
#             d[root.val] = root
        
#         queue = d.values()
#         len_q = len(queue)
#         while len(queue) > 1:
#             for root in trees:
#                 if root.left and root.left.val in d:
#                     root.left = d[root.left.val]
#                     del d[root.left.val]
#                 if root.right and root.right.val in d:
#                     root.right = d[root.right.val]
#                     del d[root.right.val]
#             if len_q == len(queue): return None
#             queue = d.values()
#         queue = list(queue)
#         if queue:
#             if self.is_valid(queue[0]):
#                 return queue[0]
#             else:
#                 return
#         else:
#             return
            
    
#     def is_valid(self, root):
#         curr, prev, stack = root, float('-inf'), []
#         while curr or stack:
#             while curr:
#                 stack.append(curr)
#                 curr = curr.left
#             curr = stack.pop()
#             if prev >= curr.val: return False
#             prev = curr.val
#             curr = curr.right
#         return True
        