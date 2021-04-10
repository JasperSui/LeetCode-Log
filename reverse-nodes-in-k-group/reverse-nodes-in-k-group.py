# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head: return None
        i = 0
        a = b = head
        while b and i < k:
            i += 1
            b = b.next
        if i < k: return head
        new_head = self.reverse(a, b)
        a.next = self.reverseKGroup(b, k)
        return new_head
        
    def reverse(self, a, b):
        curr, prev = a, None
        while curr != b:
            curr.next, prev, curr = prev, curr, curr.next
        return prev