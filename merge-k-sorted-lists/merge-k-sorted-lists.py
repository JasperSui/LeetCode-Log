# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        curr = head = ListNode()
        queue = []
        for l in lists:
            if l:
                heapq.heappush(queue, (l.val, id(l), l))
        while queue:
            _, _, curr.next = heapq.heappop(queue)
            curr = curr.next
            if curr.next:
                heapq.heappush(queue, (curr.next.val, id(curr.next), curr.next))
        return head.next