# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr_fast = head
        curr_slow = head
        while (curr_fast and curr_fast.next):
            curr_slow = curr_slow.next
            curr_fast = curr_fast.next.next
            if (curr_slow == curr_fast):
                return True
        return False
        
        