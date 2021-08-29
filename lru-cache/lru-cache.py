class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
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
        node = Node(key, value)
        self.d[key] = node
        self._append(node)
        if len(self.d) > self.size:
            n = self.head.next
            self.head.next = n.next
            n.next.prev = self.head
            del self.d[n.key]
        
    
    def _append(self, node):
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node
    
    def _remove(self, node):
        p, n = node.prev, node.next
        p.next = n
        n.prev = p


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)