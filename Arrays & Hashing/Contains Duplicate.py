def containsDuplicate(nums):
    s = set()
    i = 0
    while i < len(nums) and nums[i] not in s:
        s.add(nums[i])
        i += 1
    return i != len(nums)