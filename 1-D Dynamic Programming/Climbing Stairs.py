def climbStairs(n):
    res = [1, 1]
    for i in range(2, n + 1):
        res.append(res[i - 1] + res[i - 2])
    return res[n]


def climbStairsOptimised(n):
    # Memory optimised
    if n <= 3:
        return n

    way1, way2 = 2, 3
    for i in range(4, n + 1):
        way1, way2 = way2, way1 + way2
    return way2