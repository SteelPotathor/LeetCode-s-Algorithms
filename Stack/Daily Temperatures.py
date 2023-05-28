def dailyTemperatures(temperatures):
    stack = []
    res = [0 for i in range(len(temperatures))]
    for i, temp in enumerate(temperatures):
        while stack and temp > stack[-1][0]:
            sol = stack.pop()
            res[sol[1]] = i - sol[1]
        stack.append([temp, i])
    return res