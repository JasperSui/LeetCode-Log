class TrieNode:
    def __init__(self):
        self.links = defaultdict(TrieNode)
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.max_count = 0
        self.res = ""
    
    def insert(self, word):
        node = self.root
        for c in word:
            node = node.links[c]
        node.count += 1
        if node.count > self.max_count:
            self.max_count = node.count
            self.res = word

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = re.findall('\w+', paragraph.lower())
        banned = set(banned)
        t = Trie()
        for word in words:
            if word in banned: continue
            t.insert(word)
        return t.res