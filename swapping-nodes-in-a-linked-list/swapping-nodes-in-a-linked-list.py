# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        fast = slow = head
        for _ in range(k-1):
            fast = fast.next
        
        first = fast
        
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        second = slow
        
        first.val, second.val = second.val, first.val
        return head