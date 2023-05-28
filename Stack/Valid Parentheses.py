def isValid(s):
    stack = []

    for c in s:
        if c == "{" or c == "[" or c == "(":
            stack.append(c)
        elif len(stack) > 0:
            if stack[-1] == "{" and c != "}" or stack[-1] == "[" and c != "]" or stack[-1] == "(" and c != ")":
                return False
            else:
                stack.pop()
    return len(stack) == 0
