import collections


def maxSlidingWindow(nums, k):
    res = []
    l, r = 0, 0
    queue = collections.deque()

    while r < len(nums):
        while queue and nums[queue[-1]] < nums[r]:
            queue.pop()
        queue.append(r)
        print(queue)
        if l > queue[0]:
            queue.popleft()

        if r + 1 >= k:
            res.append(nums[queue[0]])
            l += 1
        r += 1
    return res


print(maxSlidingWindow([3, 7, 8, 9, 4], 3))
