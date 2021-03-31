# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1, s2 = [], []
        carry = 0
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next

        head = None
        while s1 or s2 or carry:
            d1 = s1.pop() if s1 else 0
            d2 = s2.pop() if s2 else 0
            carry, digit = divmod(d1 + d2 + carry, 10)
            new_head = ListNode(digit)
            new_head.next = head
            head = new_head
        return head
            