# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # prev1 = None
        # curr1 = head1

        # while curr1:
        #     nxt1=curr1.next
        #     curr1.next = prev1
        #     prev1 = curr1
        #     curr1 = nxt1
        

        # prev2 = None
        # curr2 = head2
        # while curr2:
        #     nxt2=curr2.next
        #     curr2.next = prev2
        #     prev2 = curr2
        #     curr2 = nxt2
        
        # dummy = ListNode()
        # while l1 and l2:
        #     suma = l1.val+l2.val
        #     dummy.next = ListNode(suma)
        #     l1 = l1.next
        #     l2 = l2.next
        # return dummy.next

        dummy = ListNode()
        curr=dummy
        carry = 0

        while l1 or l2:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            val = v1+v2+carry
            carry = val//10
            val = val%10
            curr.next = ListNode(val)
            curr = curr.next

            l1=l1.next if l1 else None
            l2=l2.next if l2 else None

        if carry>0:
            curr.next = ListNode(carry)
        return dummy.next

        