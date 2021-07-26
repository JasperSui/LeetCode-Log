class TrieNode:
    def __init__(self):
        self.links = defaultdict(TrieNode)
        self.is_word = False
        self.word = ""

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for c in word:
            node = node.links[c]
        node.is_word = True
        node.word = word
    
    def find(self, word):
        node = self.root
        for c in word:
            if c not in node.links.keys(): return word
            node = node.links[c]
            if node.is_word:
                return node.word

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        t = Trie()
        res = []
        for word in dictionary:
            t.insert(word)
        for word in sentence.split(' '):
            new_word = t.find(word)
            if not new_word: new_word = word
            res.append(new_word)
        return " ".join(res)