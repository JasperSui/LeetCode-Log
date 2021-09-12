class TrieNode:
    def __init__(self):
        self.links = defaultdict(TrieNode)
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for c in word:
            node = node.links[c]
        node.is_word = True
    
    def search(self, word, remain, node=None):
        if not node:
            node = self.root
        
        if not word:
            if not remain and node.is_word:
                return True
            return False
        
        for key in node.links.keys():
            if key == word[0]:
                if self.search(word[1:], remain, node.links[key]):
                    return True
            elif remain == 1:
                if self.search(word[1:], 0, node.links[key]):
                    return True
        return False
        
class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.t = Trie()

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.t.insert(word)

    def search(self, searchWord: str) -> bool:
        return self.t.search(searchWord, 1)


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)