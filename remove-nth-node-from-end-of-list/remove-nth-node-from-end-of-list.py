# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        temp = []
        dummy = ListNode()
        dummy.next = head
        while head:
            temp.append(head)
            head = head.next
        if n == len(temp): return dummy.next.next
        else:
            if -n+1 == 0:
                temp[-n-1].next = None
            else:
                temp[-n-1].next = temp[-n+1]
            return dummy.next
            