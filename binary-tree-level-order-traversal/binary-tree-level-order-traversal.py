# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # Time: O(n)
        # Space: O(height)

        # # Recursive
        # d = defaultdict(list)
        # def dfs(node, level=0):
        #     if node:
        #         d[level].append(node.val)
        #         dfs(node.left, level+1)
        #         dfs(node.right, level+1)
        # dfs(root)
        # return list(d.values())
    
        # Iterative
        queue = deque([root])
        next_level = []
        res = []
        while queue or next_level:
            curr_level = []
            while queue:
                curr = queue.popleft()
                curr_level.append(curr)
            next_level = curr_level
            if next_level:
                temp_list = []
                for n in next_level:
                    if n:
                        temp_list.append(n.val)
                        if n.left: queue.append(n.left)
                        if n.right: queue.append(n.right)
                if temp_list: res.append(temp_list)
                next_level = []
        return res
                
                
                