# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        a = b = head
        i = 0
        while b and i < k:
            b = b.next
            i += 1
        if i < k: return head
        
        new_head = self.reverse(a, b)
        a.next = self.reverseKGroup(b, k)
        return new_head
    
    def reverse(self, a, b):
        curr, prev = a, None
        while curr != b:
            curr.next, prev, curr = prev, curr, curr.next
        return prev