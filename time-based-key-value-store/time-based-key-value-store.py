class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        data = self.d.get(key, "")
        low, high = 0, len(data)
        while low < high:
            mid = (low+high) // 2
            if data[mid][0] <= timestamp: low = mid + 1
            elif data[mid][0] > timestamp: high = mid
        return "" if high == 0 else data[high-1][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)