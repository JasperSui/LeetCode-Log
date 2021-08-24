# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        original_head = dummy = ListNode()
        window_head, window_tail, dummy.next = head, head, head
        for _ in range(right - left):
            window_tail = window_tail.next
        
        for _ in range(left-1):
            original_head = original_head.next
            window_head = window_head.next
            window_tail = window_tail.next
        
        original_tail = window_tail.next
        original_head.next, window_tail.next = None, None
        new_head, new_tail = self.reverse(window_head)
        original_head.next, new_tail.next = new_head, original_tail
        
        return dummy.next
        
        
    def reverse(self, head):
        curr, tail, prev = head, head, None
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        return prev, tail
        
        