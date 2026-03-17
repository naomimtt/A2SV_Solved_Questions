# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        head2 = head
        while head2 != None:
            if len(stack) == 0:
                stack.append(head2.val)
            else:
                while stack and head2.val > stack[-1] :
                    stack.pop(-1)
                stack.append(head2.val)
            head2 = head2.next

        
        head3 = ListNode(stack[0])
        head4 = head3
    
        for i in range(1, len(stack)):
            new = ListNode(stack[i])
            head4.next = new
            head4 = new
        
        return head3


            
