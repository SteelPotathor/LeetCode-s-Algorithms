def twoSum(nums, target):
    dict = {nums[0]: 0}
    i = 1
    goal = target - nums[1]
    while i < len(nums) and goal not in dict:
        dict[nums[i]] = i
        i += 1
        goal = target - nums[i]
    return [dict.get(goal), i]