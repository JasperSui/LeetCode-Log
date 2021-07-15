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
        
        curr, prev = slow, None
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        
        while prev:
            if prev.val != head.val: return False
            prev = prev.next
            head = head.next
        return True