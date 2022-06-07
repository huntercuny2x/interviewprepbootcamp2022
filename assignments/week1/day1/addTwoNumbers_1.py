# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode()
        a = l1
        b = l2
        curr = dummyHead
        
        carry = 0
        
        while a != None or b != None:
            x = a.val if a != None else 0
            y = b.val if b != None else 0
            
            val = x + y + carry
            carry = val // 10
            
            curr.next = ListNode(val%10)
            
            curr = curr.next
            
            if a != None:
                a = a.next
            if b != None:
                b = b.next
          
        #check if we need to make a new node for another digit
        if (carry > 0):
            curr.next = ListNode(carry)
        
        return dummyHead.next
