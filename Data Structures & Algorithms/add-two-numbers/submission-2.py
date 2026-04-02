# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def add(n1,n2,n3=0):
    total = n1+n2+n3
    carry = total//10
    principal = total%10
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
                
            n1 = l1.val if l1 else 0
            n2 = l2.val if l2 else 0
            result.val, carry = add(n1,n2,carry)
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        return result_head

        