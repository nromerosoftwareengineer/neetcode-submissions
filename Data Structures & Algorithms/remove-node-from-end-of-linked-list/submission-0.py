# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        ptr = head

        length =0 

        while ptr:


            length = length +1 
            ptr = ptr.next

        
        k = length - n
        current = 0
        ptr = head
        while current < k:
            ptr = ptr.next
            current +=1


        # remove ptr
        left = head

        if left == ptr:
            left = left.next
            return left


        while not left.next == ptr:

            left = left.next

        tmp = ptr.next

        left.next = tmp
        ptr.next = None
        ptr = None

        return head 


        





        