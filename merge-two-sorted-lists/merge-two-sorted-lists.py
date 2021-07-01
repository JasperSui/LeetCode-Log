# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2: return l1
        dummy = l3 = ListNode()
        dummy.next = l3
        while l1 or l2:
            if not l1:
                v = l2.val
                l2 = l2.next
            
            elif not l2:
                v = l1.val
                l1 = l1.next
            
            else:
                if l1.val <= l2.val:
                    v = l1.val
                    l1 = l1.next
                else:
                    v = l2.val
                    l2 = l2.next
            l3.next = l3 = ListNode(v)
        return dummy.next