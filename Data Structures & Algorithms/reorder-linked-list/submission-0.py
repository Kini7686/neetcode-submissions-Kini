# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow=fast=head
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next

        second = slow.next
        prev= slow.next = None
        while second:
            tmp=second.next
            second.next = prev
            prev = second
            second = tmp
        
        first,second = head,prev
        while first and second:
            t=first.next
            q=second.next
            first.next=second
            second.next=t
            first=t
            second =q
        