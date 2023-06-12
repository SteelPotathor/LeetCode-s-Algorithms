class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.previous = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next = self.right
        self.right.previous = self.left

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

    def insert(self, node):
        previous, next = self.right.previous, self.right
        previous.next = next.previous = node
        node.next, node.previous = next, previous

    def remove(self, node):
        next, previous = node.next, node.previous
        next.previous = previous
        previous.next = next