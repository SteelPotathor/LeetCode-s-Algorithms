def permute(nums):
    res = []
    sol = []

    def backtrack(used):
        if len(sol) == len(nums):
            res.append(sol.copy())
        else:
            for i, j in enumerate(nums):
                if not used[i]:
                    sol.append(j)
                    used[i] = True
                    backtrack(used)
                    sol.pop()
                    used[i] = False

    backtrack([False] * len(nums))
    return res


print(permute([1, 2, 3]))