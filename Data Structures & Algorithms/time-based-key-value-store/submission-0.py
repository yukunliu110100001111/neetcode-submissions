from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.dic = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        values = self.dic.get(key)

        if not values:
            return ""

        res = ""
        left, right = 0, len(values) - 1

        while left <= right:
            m = left + (right - left) // 2

            if values[m][1] <= timestamp:
                res = values[m][0]
                left = m + 1
            else:
                right = m - 1

        return res