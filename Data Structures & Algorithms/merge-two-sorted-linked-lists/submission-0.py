# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        combined = None
        combined_head = None
        while (list1 is not None) or (list2 is not None):

            if list1 is None:
                selected = list2
                list2 = list2.next
            elif list2 is None:
                selected = list1
                list1 = list1.next
            else:    
                if list1.val <= list2.val:
                    selected = list1
                    list1 = list1.next
                else:
                    selected = list2
                    list2 = list2.next

            if combined is None:
                combined = selected
                combined_head = selected
                selected.next = None
            else:
                combined.next = selected
                combined = selected
                selected.next = None    

        return combined_head



            