# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:



        stack = []

        left = head.next


        while left:
            stack.append(left)
            left = left.next

        

        left = head

        odd = True
        while len(stack) > 0: 
            
            if odd:

                left.next = stack.pop(-1)
                odd = False
            else:
                odd = True
                left.next = stack.pop(0)
            left = left.next
        left.next = None


        
        
        
        
        
        
        
        