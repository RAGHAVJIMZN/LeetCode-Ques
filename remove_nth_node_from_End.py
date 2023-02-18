# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode: 
        a1 = a2 = head
        lenLL = 0
        while head:
            lenLL += 1
            head=head.next
        head = a1
        if n == lenLL:
            head = head.next
            return head
        tlength = 1
        while tlength < (lenLL-n):
            tlength += 1
            head = head.next
        if head:
            head.next = head.next.next
        return a1