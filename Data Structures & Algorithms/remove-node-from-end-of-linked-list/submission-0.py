# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if n == 0:
            temp = head
            head = head.next
            return head
        if n == 1 and head.next is None:
            return head.next
        
        curr, prev = head, None
        count = 0
        while count < n and curr:
            prev = curr
            curr = curr.next
            count += 1

        prev.next = curr.next

        return head
        
