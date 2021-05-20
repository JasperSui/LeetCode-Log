# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        # curr = dummy = ListNode(0)
        # while head:
        #     if curr.val > head.val:
        #         curr = dummy
        #     while curr.next and curr.next.val < head.val:
        #         curr = curr.next
        #     curr.next, curr.next.next, head = head, curr.next, head.next
        # return dummy.next
        
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