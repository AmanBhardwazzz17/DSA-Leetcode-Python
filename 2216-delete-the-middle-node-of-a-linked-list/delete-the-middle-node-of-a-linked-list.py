# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: ListNode | None) -> ListNode | None:
        if not head.next:
            return None
        count = 0
        temp = head
        while temp:
            count += 1
            temp = temp.next
        mid = count // 2
        temp = head
        for i in range(mid - 1):
            temp = temp.next
        temp.next = temp.next.next
        return head

        