class TimeMap:

    def __init__(self):
        self.dict = {}

    def set(self, key: str, value: str, timestamp: int):
        if key not in self.dict:
            self.dict[key] = []
        self.dict[key].append([value, timestamp])

    def get(self, key: str, timestamp: int):
        res = ""
        values = self.dict.get(key, [])
        l, r = 0, len(values) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if values[mid][1] == timestamp:
                return values[mid][0]
            elif values[mid][1] < timestamp:
                res = values[mid][0]
                l = mid + 1
            elif values[mid][1] > timestamp:
                r = mid - 1
        return res
