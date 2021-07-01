# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        curr = head = ListNode()
        pq = []
        for l in lists:
            if l:
                heapq.heappush(pq, (l.val, id(l), l))

        while pq:
            _, _, curr.next = heapq.heappop(pq)
            curr = curr.next
            if curr.next:
                heapq.heappush(pq, (curr.next.val, id(curr.next), curr.next))
        return head.next
            