def minCostClimbingStairs(cost):
    for i in range(len(cost) - 3, - 1, -1):
        cost[i] += min(cost[i + 1], cost[i + 2])
    print(cost)
    return min(cost[0], cost[1])


print(minCostClimbingStairs([10, 15, 20]))