# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        else:
            newHead = self.reverseList(head.next) # newHead is old tail, head is second to last
            # Attach curr head to the tail of our reversed list
            head.next.next = head
            head.next = None
            return newHead # The new_head of reversed list is passed upwards


