# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        node = None
        while slow:
            next, slow.next = slow.next, node
            node, slow = slow, next

        while node:
            if node.val != head.val:
                return False
            node = node.next
            head = head.next
        return True