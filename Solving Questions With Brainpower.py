def mostPoints(questions):
    res = [0 for i in range(len(questions) + 1)]
    for i in range(len(questions) - 1, -1, -1):
        res[i] = max(res[i + 1], questions[i][0] + res[min(len(questions), i + questions[i][1] + 1)])
    return res[0]