# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if len(lists) <1:
            return None
        

        def mergeTwoLists( nodeOne, nodeTwo): 

            dummy = ListNode()
            ans = dummy
            while nodeOne and nodeTwo:

                if nodeOne.val > nodeTwo.val:
                    tmp = nodeTwo.next
                    nodeTwo.next = None 

                    dummy.next = nodeTwo
                    nodeTwo = tmp
                else:
                    tmp = nodeOne.next
                    nodeOne.next = None

                    dummy.next = nodeOne
                    nodeOne =tmp
                dummy = dummy.next

            while nodeOne:

                tmp =nodeOne.next
                nodeOne.next = None

                dummy.next = nodeOne
                nodeOne = tmp

                dummy = dummy.next 

            while nodeTwo:

                tmp = nodeTwo.next

                nodeTwo.next = None

                dummy.next = nodeTwo

                nodeTwo = tmp

                dummy = dummy.next

            return ans.next 
        while len(lists) > 1:
            merged = []
            for i in range(0 , len(lists), 2):
                
                listOne = lists[i]
                listTwo = lists[i +1] if (i+1) < len(lists) else None
                combined = mergeTwoLists(listOne, listTwo)
                merged.append(combined)
            lists = merged

        return lists[0] if len(lists) >0 else None

        