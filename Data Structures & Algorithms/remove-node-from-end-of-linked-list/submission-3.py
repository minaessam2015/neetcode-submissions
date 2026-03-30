# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        curr = head
        counter = 1
        potential_prev, potential = head, None
        while curr.next:

            if counter == n+1:
                potential_prev = potential_prev.next
                potential = potential_prev.next
                counter-=1

            counter += 1
            curr = curr.next
        if counter<=n:
            return head.next
        if potential_prev.next:
            potential_prev.next = potential_prev.next.next
        else:
            head = None
        return head
        

            

