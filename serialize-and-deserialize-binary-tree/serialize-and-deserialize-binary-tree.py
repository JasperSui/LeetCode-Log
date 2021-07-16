# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        queue = deque([root])
        while queue:
            curr = queue.popleft()
            if curr:
                res.append(str(curr.val))
                queue.append(curr.left)
                queue.append(curr.right)
            else:
                res.append("#")
        return " ".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data: return
        data = deque(data.split(' '))
        root_val = data.popleft()
        if root_val == "#": return
        root = TreeNode(int(root_val))
        queue = deque([root])
        while data and queue:
            curr = queue.popleft()
            if curr:
                l, r = data.popleft(), data.popleft()
                curr.left = TreeNode(int(l)) if l != "#" else None
                curr.right = TreeNode(int(r)) if r != "#" else None
                queue.append(curr.left)
                queue.append(curr.right)
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))