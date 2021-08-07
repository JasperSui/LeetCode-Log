# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return
        
        curr = tail = head
        _len = 1
        while tail.next:
            _len += 1
            tail = tail.next
        
        k %= _len
        
        tail.next = head
        
        for _ in range(_len - k - 1):
            curr = curr.next
        
        res = curr.next
        curr.next = None
        return res
        