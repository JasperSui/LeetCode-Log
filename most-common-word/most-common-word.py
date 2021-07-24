class TrieNode:
    def __init__(self):
        self.word = ""
        self.count = 0
        self.links = [None] * 26

class Solution:
    def __init__(self):
        self.res = ""
        self.max_count = 0
    
    def insert(self, node, word):
        curr = node
        for c in word:
            index = ord(c) - ord('a')
            if not curr.links[index]:
                curr.links[index] = TrieNode()
                curr.links[index].word = curr.word + c
            curr = curr.links[index]
        curr.count += 1
    
    def ban(self, node, word):
        curr = node
        for c in word:
            index = ord(c) - ord('a')
            if not curr.links[index]: return
            curr = curr.links[index]
        curr.count = 0
    
    def find_max(self, node):
        if not node: return
        if node.count > self.max_count:
            self.res = node.word
            self.max_count = node.count
        for i in range(len(node.links)):
            self.find_max(node.links[i])
    
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        root = TrieNode()
        words = re.findall(r'\w+', paragraph.lower())
        for word in words:
            self.insert(root, word)
        for banned_word in banned:
            self.ban(root, banned_word)
        self.find_max(root)
        return self.res