# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # Time: O(N)
        # Space: O(height)
        
        # Recursive
        def is_mirror(r1, r2):
            if not r1 and not r2: return True
            elif not r1 or not r2: return False
            return r1.val == r2.val and \
                   is_mirror(r1.left, r2.right) and \
                   is_mirror(r1.right, r2.left)
        return is_mirror(root.left, root.right)
        
        # queue = deque()
        # l, r = deque(), deque()
        # queue.append((root, "qq"))
        # while queue:
        #     curr, is_left = queue.popleft()
        #     if is_left == True:
        #         if curr:
        #             l.append(curr.val)
        #             queue.append((curr.left, True))
        #             queue.append((curr.right, True))
        #         else:
        #             l.append(0)
        #     elif is_left == False:
        #         if curr:
        #             r.append(curr.val)
        #             queue.append((curr.right, False))
        #             queue.append((curr.left, False))
        #         else:
        #             r.append(0)
        #     else:
        #         queue.append((curr.left, True))
        #         queue.append((curr.right, False))
        #     if l and r:
        #         if len(l) == len(r) and l[-1] != r[-1]:
        #             return False
        # if len(l) != len(r): return False
        # return True
            