def minCostClimbingStairs(cost):
    res = [cost[i] for i in range(len(cost))]
    for i in range(len(cost) - 3, -1, -1):
        res[i] += min(res[i + 1], res[i + 2])
    return min(res[0], res[1])


def minCostClimbingStairs2(cost):
    res = [cost[i] for i in range(len(cost))]
    for i in range(2, len(cost)):
        res[i] += min(res[i - 2], res[i - 1])
    return min(res[-1], res[-2])
