def carFleet(target, position, speed):
    stack = []

    posAndSpeed = [(p, s) for p,s in zip(position, speed)]
    posAndSpeed.sort(reverse=True)

    for i in range(len(posAndSpeed)):
        arrival = (target - posAndSpeed[i][0]) / posAndSpeed[i][1]
        while stack and arrival < stack[-1]:
            stack.pop()
        stack.append(arrival)
    return len(stack)

print(carFleet(100, [0,2,4],[4,2,1]))