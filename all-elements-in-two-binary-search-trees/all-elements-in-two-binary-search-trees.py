# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        self.l1 = deque()
        self.l2 = deque()
        res = []
        def dfs(node, l):
            if not node: return
            dfs(node.left, l)
            l.append(node.val)
            dfs(node.right, l)
        dfs(root1, self.l1)
        dfs(root2, self.l2)
        while self.l1 or self.l2:
            if not self.l1:
                res.append(self.l2.popleft())
            elif not self.l2:
                res.append(self.l1.popleft())
            if self.l1 and self.l2:
                n1 = self.l1[0]
                n2 = self.l2[0]
                if n1 > n2:
                    res.append(self.l2.popleft())
                else:
                    res.append(self.l1.popleft())
        return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        self.l1 = deque()
        self.l2 = deque()
        res = []
        def dfs(node, l):
            if not node: return
            dfs(node.left, l)
            l.append(node.val)
            dfs(node.right, l)
        dfs(root1, self.l1)
        dfs(root2, self.l2)
        while self.l1 or self.l2:
            if not self.l1:
                res.append(self.l2.popleft())
            elif not self.l2:
                res.append(self.l1.popleft())
            elif self.l1 and self.l2:
                n1 = self.l1[0]
                n2 = self.l2[0]
                if n1 > n2:
                    res.append(self.l2.popleft())
                else:
                    res.append(self.l1.popleft())
        return res