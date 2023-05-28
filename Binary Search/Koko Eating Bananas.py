import math


def minEatingSpeed(piles, h):
    maxBananas = max(piles)
    if len(piles) == h:
        return maxBananas
    else:
        res = 0
        l, r = 1, maxBananas
        while l <= r:
            mid = l + (r - l) // 2
            if eatingPossible(piles, h, mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
    return res


def eatingPossible(piles, h, bananasPerHour):
    time, i = 0, 0
    while i < len(piles) and time < h:
        time += math.ceil(piles[i] / bananasPerHour)
        i += 1
    return i == len(piles) and time <= h