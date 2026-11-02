# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class NodeWrap:
    def __init__(self,node):
        self.node = node
    
    def __lt__(self,nodewrap):
        return self.node.val < nodewrap.node.val
 
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode(0)
        cur = head
        heap = []
        for i in lists:
            if i is not None:
                 heapq.heappush(heap, NodeWrap(i))
        
        while heap:
            node_wrap = heapq.heappop(heap)
            cur.next = node_wrap.node
            cur = cur.next

            if node_wrap.node.next:
                heapq.heappush(heap,NodeWrap(node_wrap.node.next))
        return head.next




