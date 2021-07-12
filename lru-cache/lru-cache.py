class Node:
    def __init__(self, k, v):
        self.key = k
        self.value = v
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.d = dict()
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.d:
            node = self.d[key]
            self._remove(node)
            self._append(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self._remove(self.d[key])
        n = Node(key, value)
        self.d[key] = n
        self._append(n)
        if len(self.d) > self.size:
            last = self.head.next
            self._remove(last)
            del self.d[last.key]
    
    def _append(self, node):
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail
    
    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)