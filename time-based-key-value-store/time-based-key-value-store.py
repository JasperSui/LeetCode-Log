class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        data = self.d[key]
        if not data: return ""
        if len(data) == 1: return data[0][0]
        low, high = 0, len(data)
        while low < high:
            mid = low + (high - low) // 2
            if data[mid][1] < timestamp:
                low = mid + 1
            elif data[mid][1] > timestamp:
                high = mid
            else:
                return data[mid][0]
        return "" if high == 0 else data[high-1][0]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)