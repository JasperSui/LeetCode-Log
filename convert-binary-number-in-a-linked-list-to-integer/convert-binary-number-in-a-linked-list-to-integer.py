# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        # res = ""
        # while head:
        #     res += str(head.val)
        #     head = head.next
        # return int(res, 2)
        
        ans = 0
        while head:
            # 等於往左推一個bit，高位拋棄，低位補0，最後 | 就是再加上10進位制的
            # 4 (100) << 1 就變成 8 (1000), 6 (110) << 1 就變成 12 (1100)
            ans = (ans << 1) | head.val
            head = head.next
        return ans