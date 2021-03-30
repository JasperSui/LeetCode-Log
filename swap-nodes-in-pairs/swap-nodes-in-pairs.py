# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # Time: O(n)
        # Space: O(n)
        dummy = ListNode()
        dummy.next = head
        cur = dummy
        while cur.next and cur.next.next:
            a, b = cur.next, cur.next.next
            cur.next = b
            a.next = b.next
            b.next = a
            cur = cur.next.next
        return dummy.next