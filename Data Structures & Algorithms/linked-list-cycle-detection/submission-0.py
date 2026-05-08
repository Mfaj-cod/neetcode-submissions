# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        
        nodes = set()
        curr = head
        while curr:
            if curr in nodes:
                return True
            else:
                nodes.add(curr)
            curr = curr.next
        
        return False