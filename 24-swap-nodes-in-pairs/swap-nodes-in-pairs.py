# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        if not head or not head.next:
            return head    
        temp = head
        head = head.next  # नया head अब दूसरा नोड होगा
        prev = None
        while None != temp and None != temp.next:
            nxt = temp.next
            self.swapNodes(prev, temp, nxt)
            prev = temp
            temp = temp.next     
        return head
    def swapNodes(self, prev, a, b):
        a.next = b.next
        b.next = a
        if prev:
            prev.next = b
