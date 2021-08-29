# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = insert_node = head
        while head and head.next:
            if head.val > head.next.val:
                insert_node = head.next
                pre_insert_node = dummy
                while pre_insert_node.next.val < insert_node.val:
                    pre_insert_node = pre_insert_node.next
                head.next = insert_node.next
                insert_node.next = pre_insert_node.next
                pre_insert_node.next = insert_node
            else:
                head = head.next
        return dummy.next