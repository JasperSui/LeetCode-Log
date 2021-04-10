# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode, prev=None) -> ListNode:
        # Time: O(n)
        # Space: O(n)
        
        # curr, prev = head, None
        # while curr:
        #     curr.next, prev, curr = prev, curr, curr.next
        # return prev
        
        curr, prev = head, None
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        return prev