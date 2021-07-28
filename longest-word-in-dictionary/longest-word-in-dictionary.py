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
    
    def bfs(self):
        queue = deque([self.root])
        res = ""
        while queue:
            curr = queue.popleft()
            for node in curr.links.values():
                if node.is_word:
                    queue.append(node)
                    if len(node.word) > len(res) or node.word < res:
                        res = node.word
        return res
        

class Solution:
    def longestWord(self, words: List[str]) -> str:
        t = Trie()
        for word in words:
            t.insert(word)
        return t.bfs()