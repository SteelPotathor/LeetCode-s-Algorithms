def canJump(nums):
    i = 1
    jumpCap = nums[0]
    while i < len(nums) and jumpCap >= 1:
        if nums[i] >= jumpCap - 1:
            jumpCap = nums[i]
        else:
            jumpCap -= 1
        i += 1
    return i == len(nums)
