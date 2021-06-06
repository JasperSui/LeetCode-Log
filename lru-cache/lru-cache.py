class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.d = dict()
        self.queue = deque()

    def get(self, key: int) -> int:
        try:
            value = self.d[key]
        except:
            value = -1
        else:
            self.queue.remove(key)
            self.queue.appendleft(key)
        return value

    def put(self, key: int, value: int) -> None:
        if len(self.queue) == self.size:
            if key in self.queue:
                self.queue.remove(key)
            else:
                deleted_key = self.queue.pop()
                del self.d[deleted_key]
            
        else:
            if key in self.queue:
                self.queue.remove(key)
        self.queue.appendleft(key)
        self.d[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)