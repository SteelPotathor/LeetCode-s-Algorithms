def rob(nums):
    rob1, rob2 = 0, 0
    for n in nums:
        rob1, rob2 = rob2, max(n + rob1, rob2)
    return rob2


def rob2(nums):
    if len(nums) >= 2:
        res = [nums[0], max(nums[0], nums[1])]
        for i in range(2, len(nums)):
            res.append(max(res[-1], res[-2] + nums[i]))
        return res[-1]
    else:
        return nums[0]