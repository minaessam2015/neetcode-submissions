# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        list_dict = {}
        counter = 0
        curr = head
        while curr is not None:
            list_dict[counter] = curr
            curr = curr.next
            counter+=1
        
        s,e = 0, counter-1
        switch = True
        curr_node = head
        for i in range(counter):
            if switch:
                ele = list_dict[e]
                s+=1
            else:
                ele = list_dict[s]
                e-=1
            switch = not switch
            curr_node.next = ele
            curr_node = ele
        curr_node.next = None

    def reorderList(self, head: Optional[ListNode]) -> None:
        middle = None
        slow,fast = head, head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # Reverse
        prev,middle = None, slow.next
        slow.next = None
        while middle is not None:
            tmp = middle.next
            middle.next = prev
            prev = middle
            middle = tmp

        curr = head
        slow = prev
        while slow is not None:
            first, second, third, fourth = curr, slow, curr.next, slow.next
            first.next = second
            second.next = third
            slow = fourth
            curr = third



            





        
