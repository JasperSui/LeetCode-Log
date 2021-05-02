# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = l3 = ListNode()
        while l1 or l2:
            if l1 and l2:
                if l1.val <= l2.val:
                    val = l1.val
                    l1 = l1.next
                else:
                    val = l2.val
                    l2 = l2.next
            elif l1:
                val = l1.val
                l1 = l1.next
            else:
                val = l2.val
                l2 = l2.next
            l3.next = ListNode(val)
            l3 = l3.next
        return res.next