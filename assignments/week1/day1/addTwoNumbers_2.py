# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        counter = 0
        num1 = 0
        num2 = 0
        while(l1):
            num1 += pow(10, counter) * l1.val
            counter+=1
            l1=l1.next
        counter = 0
        while(l2):
            num2 += pow(10, counter) * l2.val
            counter+=1
            l2=l2.next
            
        result = num1 + num2
        
        head = ListNode()
        current = head
        
        while(result > 0):
            current.val = result%10
            result = result//10
            
            if(result != 0):
                n = ListNode()
                current.next = n
                current = current.next
        
        return head
