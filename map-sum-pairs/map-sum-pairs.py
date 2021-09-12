class TrieNode:
    def __init__(self):
        self.links = defaultdict(TrieNode)
        self.points = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word, points):
        node = self.root
        for c in word:
            node = node.links[c]
        node.points = points
    
    def get_points(self, node):
        points = node.points
        for child in node.links.values():
            points += self.get_points(child)
        return points
    
    def find(self, word):
        depth = 0
        node = self.root
        if not word:
            return self.get_points
        for c in word:
            if c not in node.links: return 0
            depth += 1
            node = node.links[c]
            if depth == len(word):
                return self.get_points(node)
        return 0
        
        
class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.t = Trie()

    def insert(self, key: str, val: int) -> None:
        self.t.insert(key, val)
        
    def sum(self, prefix: str) -> int:
        return self.t.find(prefix)


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)