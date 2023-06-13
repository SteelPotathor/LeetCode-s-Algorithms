def combinationSum2(candidates, target):
    candidates.sort()
    res = []
    sol = []

    def backtrack(index, total):
        if total == target:
            res.append(sol.copy())
        elif total < target:
            previous = -1
            for i in range(index, len(candidates)):
                if candidates[i] != previous:
                    sol.append(candidates[i])
                    backtrack(i + 1, total + candidates[i])
                    sol.pop()
                    previous = candidates[i]

    backtrack(0, 0)
    return res


print(combinationSum2([1, 2, 2, 2, 5], 5))
