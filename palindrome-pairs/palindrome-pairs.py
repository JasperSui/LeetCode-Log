class TrieNode:
    def __init__(self):
        self.index = -1
        self.p_below = []
        self.links = defaultdict(TrieNode)
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, word, index):
        node = self.root
        for i, c in enumerate(reversed(word)):
            if self.is_p(word[:len(word)-i]):
                node.p_below.append(index)
            node = node.links[c]
        node.index = index
    
    def search(self, word, index, res):
        node = self.root
        for i, c in enumerate(word):
            if node.index >= 0 and index != node.index and self.is_p(word[i:]):
                res.append([index, node.index])
            node = node.links.get(c)
            if not node: return res
        
        for p in node.p_below:
            if p != index:
                res.append([index, p])
        
        if node.index >= 0 and index != node.index:
            res.append([index, node.index])
        return res
    
    def is_p(self, word):
        i, j = 0, len(word) - 1
        while i < j:
            if word[i] != word[j]: return False
            i += 1
            j -= 1
        return True

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        res = []
        t = Trie()
        for i, word in enumerate(words):
            t.add(word, i)
        for i, word in enumerate(words):
            res = t.search(word, i, res)
        return res