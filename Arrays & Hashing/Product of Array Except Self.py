def productExceptSelf(nums):
    answer = [1 for i in range(len(nums))]
    prefix, postfix = 1, 1

    for i in range(len(nums)):
        answer[i] *= prefix
        prefix *= nums[i]

    for i in range(len(nums) - 1, -1, -1):
        answer[i] *= postfix
        postfix *= nums[i]

    return answer