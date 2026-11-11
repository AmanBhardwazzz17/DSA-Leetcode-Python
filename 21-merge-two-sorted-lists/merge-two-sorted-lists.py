# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        temp = ListNode()
        pointer = temp
        
        while list1 != None and list2 != None:
            if list1.val < list2.val:
                pointer.next = list1      # pointer की जगह pointer.next लिखें
                list1 = list1.next
            else:
                pointer.next = list2      # pointer की जगह pointer.next लिखें
                list2 = list2.next
            pointer = pointer.next
            
        if list1 == None:
            pointer.next = list2          # यहां भी pointer.next लिखें
        else:
            pointer.next = list1          # यहां भी pointer.next लिखें
            
        return temp.next                  # list1 की जगह temp.next रिटर्न करें

       