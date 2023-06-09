def findDuplicate(nums):
    slow, fast = nums[0], nums[nums[0]]
    while slow != fast:
        slow = nums[slow]
        fast = nums[nums[fast]]

    slow2 = 0
    while slow != slow2:
        slow = nums[slow]
        slow2 = nums[slow2]

    return slow


print(findDuplicate([1, 3, 4, 2, 2]))
