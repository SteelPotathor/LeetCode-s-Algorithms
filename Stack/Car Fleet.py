import random


def carFleet(target, position, speed):
    stack = []

    posAndSpeed = [(p, s) for p,s in zip(position, speed)]
    posAndSpeed.sort(reverse=True)

    for i in range(len(posAndSpeed)):
        arrival = (target - posAndSpeed[i][0]) / posAndSpeed[i][1]
        stack.append(arrival)
        if len(stack) >= 2 and arrival <= stack[-2]:
            stack.pop()
    return len(stack)