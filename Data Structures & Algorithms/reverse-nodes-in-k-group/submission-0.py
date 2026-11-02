# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        ans = ListNode(0)
        cur = ans
        stack = []
        if head is None or head.next is None:
            return head
        counter = 0

        while head:
            stack.append(head)
            counter +=1
            head = head.next

            if counter == k:
                while counter != 0:
                    cur.next = stack.pop()
                    cur = cur.next
                    counter -= 1
 
        while counter != 0:
                    cur.next = stack.pop(0)
                    cur = cur.next
                    counter -= 1
        
        cur.next = None
        
        return ans.next
        