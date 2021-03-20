# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        # Time: O(N)
        # Space: O(1)
        
        # # Solution 1 32ms
        # res = []
        # while head:
        #     res.append(str(head.val))
        #     head = head.next
        # return int(''.join(res), 2)
        
        # Solution 2
        ans = 0
        while head:
            ans = 2*ans + head.val
            head = head.next
        return ans