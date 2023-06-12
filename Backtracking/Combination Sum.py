def combinationSum(candidates, target):
    res = []
    sol = []

    def backtrack(i, total):
        if total == target:
            res.append(sol.copy())
        elif i < len(candidates) and total <= target:
            sol.append(candidates[i])
            backtrack(i, total + candidates[i])
            sol.pop()
            backtrack(i + 1, total)

    backtrack(0, 0)
    return res