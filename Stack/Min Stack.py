class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, val):
        self.stack.append(val)
        mini = min(val, self.min[-1] if self.min else val)
        self.min.append(mini)

    def pop(self):
        self.stack.pop()
        self.min.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min[-1]