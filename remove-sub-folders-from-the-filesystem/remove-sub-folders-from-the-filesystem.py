class TrieNode:
    def __init__(self):
        self.links = defaultdict(TrieNode)
        self.is_word = False
        self.word = ""

class Trie:
    
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, path):
        node = self.root
        for c in path:
            node = node.links[c]
        node.is_word = True
        node.word = "".join(["/"+c for c in path])
    
    def bfs(self):
        res = []
        queue = deque([self.root])
        while queue:
            curr = queue.popleft()
            if curr.is_word:
                res.append(curr.word)
                continue
            for node in curr.links.values():
                queue.append(node)
        return res

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        t = Trie()
        for path in folder:
            t.insert(path.split('/')[1:])
        return t.bfs()
            