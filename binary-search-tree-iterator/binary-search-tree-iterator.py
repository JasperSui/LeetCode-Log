# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.data = deque()
        def dfs(node):
            if not node: return
            dfs(node.left)
            self.data.append(node.val)
            dfs(node.right)
        dfs(root)

    def next(self) -> int:
        return self.data.popleft()
        
    def hasNext(self) -> bool:
        return len(self.data) > 0
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()