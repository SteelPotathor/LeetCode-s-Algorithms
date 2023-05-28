def searchMatrix(matrix, target):
    # Flatten the matrix into a list
    nums = []
    for row in matrix:
        nums += row

    l, r = 0, len(nums) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if nums[mid] == target:
            return True
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return False


def searchMatrixOptimised(matrix, target):
    top, bottom = 0, len(matrix) - 1
    while top <= bottom:
        mid = top + (bottom - top) // 2
        if matrix[mid][0] <= target <= matrix[mid][-1]:
            break
        elif target > matrix[mid][-1]:
            top = mid + 1
        elif target < matrix[mid][0]:
            bottom = mid - 1
    if top > bottom:
        return False

    l, r = 0, len(matrix[0]) - 1
    while l <= r:
        newMid = l + (r - l) // 2
        if matrix[mid][newMid] == target:
            return True
        elif matrix[mid][newMid] < target:
            l = newMid + 1
        elif matrix[mid][newMid] > target:
            r = newMid - 1
    return False