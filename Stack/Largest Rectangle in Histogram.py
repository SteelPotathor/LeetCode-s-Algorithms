def largestRectangleArea(heights):
    stack = []
    area = 0

    for index, height in enumerate(heights):
        start = index
        while stack and stack[-1][1] > height:
            i, h = stack.pop()
            area = max(area, (index - i) * h)
            start = i
        stack.append((start, height))

    for i, h in stack:
        area = max(area, (len(heights) - i) * h)
    return area
