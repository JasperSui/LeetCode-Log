# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        stack = []
        for l in lists:
            while l:
                stack.append(l.val)
                l = l.next
        stack.sort()
        head = None
        while stack:
            new_head = ListNode(stack.pop())
            new_head.next = head
            head = new_head
        return head