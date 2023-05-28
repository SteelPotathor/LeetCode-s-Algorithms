def trap(height):

    if not height:
        return 0

    l, r = 0, len(height) - 1
    maxL, maxR = height[l], height[r]
    res = 0

    while l < r:
        if maxL > maxR:
            r -= 1
            maxR = max(height[r], maxR)
            res += maxR - height[r]
        else:
            l += 1
            maxL = max(height[l], maxL)
            res += maxL - height[l]
    return res