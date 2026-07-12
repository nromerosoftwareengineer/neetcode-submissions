# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        tail = None
        
# 0 1 2 3  
# t h
#    tmp
        while head:

           tmp = head.next

           head.next = tail

           tail = head

           head =tmp

            
          

        
        return tail
        