from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy

        kth = self.getKth(groupPrev, k)
        while kth:
            groupNext = kth.next

            previous, current = kth.next, groupPrev.next
            while current != groupNext:
                tmp = current.next
                current.next = previous
                previous = current
                current = tmp

            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp

            kth = self.getKth(groupPrev, k)
        return dummy.next

    def getKth(self, current, k):
        while current and k > 0:
            current = current.next
            k -= 1
        return current
