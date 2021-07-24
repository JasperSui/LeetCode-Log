class TrieNode:
    def __init__(self):
        self.val = 0
        self.is_word = False
        self.links = defaultdict(TrieNode)

class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def insert(self, key: str, val: int) -> None:
        node = self.root
        for c in key:
            node = node.links[c]
        node.is_word = True
        node.val = val

        
    def sum(self, prefix: str) -> int:
        node = self.root
        for c in prefix:
            next_node = node.links[c]
            if not next_node:
                return 0
            node = next_node
        return self.dfs(node)
    
    def dfs(self, node):
        ans = 0
        for child in node.links.keys():
            ans += self.dfs(node.links[child])
        return ans + node.val

    

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)