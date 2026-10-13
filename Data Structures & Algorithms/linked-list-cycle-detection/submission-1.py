# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        ans = defaultdict()
        while head:
            if head in ans:
                return True
            ans[head] = head.val
            head = head.next
        return False