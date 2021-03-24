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
        # if not root: return []
        # d = defaultdict(list)
        # def dfs(node, level):
        #     if not node: return
        #     d[level].append(node.val)
        #     dfs(node.left, level+1)
        #     dfs(node.right, level+1)
        # dfs(root, 0)
        # return list(d.values())[::-1]
    
        # Iterative
        if not root: return []
        queue = deque([root])
        res = deque()
        next_level = []
        while queue or next_level:
            curr_level = []
            while queue:
                curr = queue.popleft()
                if curr:
                    curr_level.append(curr)
            next_level = curr_level
            if next_level:
                temp_list = []
                for n in next_level:
                    if n:
                        temp_list.append(n.val)
                        queue.append(n.left)
                        queue.append(n.right)
                if temp_list:
                    res.appendleft(temp_list)
        return list(res)
        