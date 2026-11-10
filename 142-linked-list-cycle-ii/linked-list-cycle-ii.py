# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Meeting Point
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break 
        else:
            # Loop hi nahi hai
            return None
        # Start point nikalo
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow

