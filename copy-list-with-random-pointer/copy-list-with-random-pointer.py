"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: return head
        node = head
        while node:
            copy = Node(node.val)
            copy.next = node.next
            node.next = copy
            node = copy.next
        
        node = head
        while node:
            if node.random:
                node.next.random = node.random.next
            node = node.next.next
        
        copy_head = head.next
        copy = copy_head
        while copy.next:

            copy.next = copy.next.next
            copy = copy.next 

        return copy_head