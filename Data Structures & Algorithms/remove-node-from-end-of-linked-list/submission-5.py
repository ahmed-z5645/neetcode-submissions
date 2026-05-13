# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0

        curr = head
        while curr:
            l += 1
            curr = curr.next

        if l == 1:
            return None
        
        index = l - n

        # index is correct == 0

        curr = head
        i = 0

        if index == 0:
            return head.next

        while i < index - 1:
            curr = curr.next
            i += 1

        r = curr.next
        curr.next = r.next

        return head