def subsetsWithDup(nums):
    nums.sort()
    res = []
    sol = []

    def backtrack(i):
        if i == len(nums):
            res.append(sol.copy())
        else:
            sol.append(nums[i])
            backtrack(i + 1)
            sol.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1)

    backtrack(0)
    return res