def search(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if nums[mid] == target:
            return mid

        # nums[mid] is in the right part of the sorted array
        elif nums[l] <= nums[mid]:
            if target > nums[mid] or target < nums[l]:
                l = mid + 1
            else:
                r = mid - 1

        # nums[mid] is in the left part of the sorted array
        else:
            if target < nums[mid] or target > nums[r]:
                r = mid - 1
            else:
                l = mid + 1
    return -1