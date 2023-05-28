def evalRPN(tokens):
    stack = []
    for t in tokens:
        match (t):
            case "+":
                stack.append(stack.pop() + stack.pop())
            case "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            case "*":
                stack.append(stack.pop() * stack.pop())
            case "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            case _:
                stack.append(int(t))
    return stack[0]