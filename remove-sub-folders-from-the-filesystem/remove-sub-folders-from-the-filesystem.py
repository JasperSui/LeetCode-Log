class TrieNode:
    def __init__(self):
        self.links = defaultdict(TrieNode)
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        word = word.split('/')[1:]
        node = self.root
        for c in word:
            node = node.links[c]
        node.is_word = True
    
    def bfs(self):
        res = []
        queue = deque([(self.root, [])])
        while queue:
            node, path = queue.popleft()
            if node.is_word:
                res.append("/" + "/".join(path))
                continue
            
            for c in node.links.keys():
                queue.append((node.links[c], path + [c]))
        return res

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        t = Trie()
        for word in folder:
            t.insert(word)
        return t.bfs()