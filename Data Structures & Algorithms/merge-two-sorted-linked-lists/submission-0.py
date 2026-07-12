# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = list1
        head2 = list2
        ans = ListNode(0, None)
        tail = ans




    
        while head1 and head2: 
            
            if head1.val > head2.val:
                ans.next = head2
                head2 = head2.next
                
                
            else:
                ans.next = head1
                head1 = head1.next
           
            ans = ans.next
        
        if head1 and (head2 == None):
            ans.next = head1
            
        if head2 and (head1 == None):
            ans.next = head2 
 
            

        
        return tail.next
