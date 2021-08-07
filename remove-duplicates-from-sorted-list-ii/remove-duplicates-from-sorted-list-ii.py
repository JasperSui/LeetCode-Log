# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        pre = dummy
        curr = head
        while curr:
            while curr.next and curr.val == curr.next.val:
                curr = curr.next
            if pre.next == curr:
                pre = curr
            else:
                pre.next = curr.next
            curr = curr.next
        return dummy.next