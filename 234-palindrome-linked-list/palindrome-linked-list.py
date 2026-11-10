# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        # 1. MIDDLE NIKALO
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # slow ab second half ka head hai
        # 2. SECOND HALF REVERSE KARO
        prev = None
        curr = slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        # 3. COMPARE KARO
        first = head
        second = prev # reversed second half
        while second: # sirf second half tak check karna hai
            if first.val != second.val:
                return False
            first = first.next
            second = second.next    
        return True