def findPairs(nums, k):
    dict = {}
    for n in nums:
        dict[n] = dict.get(n, 0) + 1

    counter = 0
    if k != 0:
        for key, value in dict.items():
            if k + key in dict:
                counter += 1
    else:
        for key, value in dict.items():
            if value > 1:
                counter += 1
    return counter