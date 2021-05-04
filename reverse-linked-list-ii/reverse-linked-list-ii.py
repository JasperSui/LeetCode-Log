# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        original_head = dummy = ListNode(0)
        window_head, window_tail = head, head
        dummy.next = head
        for _ in range(right-left):
            window_tail = window_tail.next
        
        for _ in range(left-1):
            original_head, window_head, window_tail = window_head, window_head.next, window_tail.next
        
        original_tail, window_tail.next = window_tail.next, None
        reversed_head, reversed_tail = self.reverse(window_head)
        
        original_head.next, reversed_tail.next = reversed_head, original_tail
        return dummy.next
    
    def reverse(self, head):
        curr, tail, prev = head, head, None
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        return prev, tail