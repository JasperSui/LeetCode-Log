# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(set)
        visited = set()
        
        def dfs(node):
            if not node: return
            if node.left:
                graph[node.val].add(node.left.val)
                graph[node.left.val].add(node.val)
                dfs(node.left)
            if node.right:
                graph[node.val].add(node.right.val)
                graph[node.right.val].add(node.val)
                dfs(node.right)
        
        dfs(root)
        res = [target.val]
        for _ in range(k):
            size, level = len(res), []
            for _ in range(size):
                curr = res.pop()
                if curr not in visited:
                    level += graph[curr]
                    visited.add(curr)
            res = level
        
        return [v for v in res if v not in visited]
                