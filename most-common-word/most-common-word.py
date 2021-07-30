class TrieNode:
    def __init__(self):
        self.count = 0
        self.word = ""
        self.links = defaultdict(TrieNode)

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.max_count = 0
        self.max_word = ""
    
    def insert(self, word):
        node = self.root
        for c in word:
            node = node.links[c]
        node.count += 1
        node.word = word
    
    def ban(self, word):
        node = self.root
        for c in word:
            node = node.links[c]
        node.count = 0
    
    def find_max(self, node=None):
        if not node: 
            node = self.root
        if node.count > self.max_count:
            self.max_count = node.count
            self.max_word = node.word
        for key in node.links.keys():
            self.find_max(node.links[key])
        return self.max_word

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        t = Trie()
        words = re.findall(r'\w+', paragraph.lower())
        for word in words:
            t.insert(word)
        for word in banned:
            t.ban(word)
        return t.find_max()