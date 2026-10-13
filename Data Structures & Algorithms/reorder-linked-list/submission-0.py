class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return

        temp = []
        while head:
            temp.append(head)
            head = head.next

        left = 0
        right = len(temp) - 1

        while left < right:
            temp[left].next = temp[right]
            left += 1

            if left == right:
                break

            temp[right].next = temp[left]
            right -= 1

        temp[left].next = None