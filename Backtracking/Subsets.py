from copy import deepcopy


def subsets(nums):
    res = []
    sol = []

    def backtrack(i):
        if i >= len(nums):
            res.append(sol.copy())
            return

        sol.append(nums[i])
        backtrack(i + 1)
        sol.pop()
        backtrack(i + 1)

    backtrack(0)
    return res


def subsets2(nums):
    res = [[], [nums[0]]]
    for n in nums[1:]:
        for i in range(len(res)):
            sol = res[i].copy()
            sol.append(n)
            res.append(sol)
    return res