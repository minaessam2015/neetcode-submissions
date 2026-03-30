# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = {}
        index = -1
        counter = 0
        while head is not None:
            if id(head) in visited:
                index = visited[id(head)]
                break
            visited[id(head)] = counter
            counter+=1
            head = head.next

        return index != -1

        