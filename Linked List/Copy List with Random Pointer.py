from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        address = {None: None}  # Key: Original Node, Value: Copied Node
        current = head

        while current:
            address[current] = Node(current.val)
            current = current.next

        current = head
        while current:
            copy = address[current]
            copy.next = address[current.next]
            copy.random = address[current.random]
            current = current.next

        return address[head]