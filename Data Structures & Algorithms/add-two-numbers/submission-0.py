# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def add(n1,n2,n3=0):
    total = n1+n2+n3
    carry = 1 if total >9 else 0
    principal = total-10 if carry else total
    return principal, carry

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        result = None
        result_head = None
        carry = 0

        while l1  or l2 or carry:
            if result is None and result_head is None:
                result  = ListNode()
                result_head = result
            
            else:
                result.next  = ListNode()
                result = result.next
                
            if l1 is None and l2 is None and carry:
                result.val, carry = add(0, carry)
            elif l1 is None:
                result.val, carry = add(l2.val, carry)
            elif l2 is None:
                result.val, carry = add(l1.val, carry)
            else:
                result.val, carry = add(l1.val, l2.val, carry)
            
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        return result_head

        