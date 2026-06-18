# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        second = dummy
        first = head
        for i in range(n): # Have the first node be n spaces ahead
            first = first.next 
        while (first): # Advance both nodes until first is null
            first = first.next
            second = second.next # Second is now right before node for removal
        second.next = second.next.next
        return dummy.next # dummy.next points to head whether removed or not
        