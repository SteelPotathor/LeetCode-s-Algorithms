def maxArea(height):
    l, r = 0, len(height) - 1
    res = 0
    h = max(height)

    while l < r:
        res = max(res, min(height[l], height[r]) * (r - l))
        if height[l] > height[r]:
            r -= 1
        else:
            l += 1
        if (r - l) * h <= res:
            break
    return res