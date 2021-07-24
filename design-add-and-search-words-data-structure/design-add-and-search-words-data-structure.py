class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def addWord(self, word: str) -> None:
        node = self.trie
        for c in word:
            if c not in node:
                node[c] = {}
            node = node[c]
        node['#'] = '#'

    def search(self, word: str, node=None) -> bool:
        if node is None:
            node = self.trie
        for i, c in enumerate(word):
            if c == '.':
                return any(self.search(word[i+1:], node[w]) for w in node if w != "#")
            if c not in node: return False
            node = node[c]
        return '#' in node

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)