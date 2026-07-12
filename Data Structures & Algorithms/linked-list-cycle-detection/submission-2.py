# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        tail = head


        while tail and head:

            tail = tail.next
            
            if head.next:

                head = head.next.next
            else:
                head = head.next

            if (tail == head) and (tail != None) and (head != None):
                return True



        return  False
        