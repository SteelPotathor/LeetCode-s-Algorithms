from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums

    def add(self, val: int) -> int:
        self.heap.append(val)

