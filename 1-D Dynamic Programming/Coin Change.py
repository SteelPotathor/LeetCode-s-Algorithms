def coinChange(coins, amount):
    res = [float("infinity") for i in range(amount + 1)]
    res[0] = 0
    for i in range(1, len(res)):
        for c in coins:
            if i - c >= 0:
                res[i] = min(res[i], res[i - c] + 1)
    return res[amount] if res[amount] != float("infinity") else -1