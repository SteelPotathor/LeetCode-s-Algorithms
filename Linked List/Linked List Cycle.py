from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s = set()
        current = head

        while current and current not in s:
            s.add(current)
            current = current.next

        return False if not current else True

    def hasCycle2(self, head: Optional[ListNode]) -> bool:
        fast, slow = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False
