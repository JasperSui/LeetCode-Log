# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        len_h = 0
        curr = head
        while curr:
            len_h += 1
            curr = curr.next

        if len_h == 1:
            return head

        first, second = None, None
        first_index, second_index = k - 1, len_h - k
        if first_index == second_index:
            return head
        curr = head
        curr_index = 0
        while curr:
            if curr_index == first_index:
                first = curr
            elif curr_index == second_index:
                second = curr
            curr_index += 1
            curr = curr.next
        first.val, second.val = second.val, first.val
        return head
        