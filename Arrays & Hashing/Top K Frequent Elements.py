import heapq


def topKFrequent(nums, k):
    dict = {}
    counter = [[] for i in range(len(nums) + 1)]

    for i in nums:
        dict[i] = 1 + dict.get(i, 0)

    for key, value in dict.items():
        counter[value].append(key)

    res = []
    for i in range(len(counter) - 1, 0, -1):
        for value in counter[i]:
            res.append(value)
            if len(res) == k:
                return res


def topKFrequent2(nums, k):
    dict = {}
    heap = []

    for i in nums:
        dict[i] = 1 + dict.get(i, 0)

    for num, freq in dict.items():
        heapq.heappush(heap, (-freq, num))

    res = []
    for i in range(k):
        res.append(heapq.heappop(heap)[1])

    return res