# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        curr = dummy
        while curr.next and curr.next.next:
            a, b = curr.next, curr.next.next
            curr.next = b
            a.next = b.next
            b.next = a
            curr = curr.next.next
        return dummy.next