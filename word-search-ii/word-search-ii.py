class TrieNode:
    def __init__(self):
        self.links = [None] * 26
        self.word = ""

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        root = self.build_trees(words)
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, i, j, root, res)
        return res
    
    def dfs(self, board, i, j, node, res):
        if not (i >= 0 and j >= 0 and i < len(board) and j < len(board[0])): return
        c = board[i][j]
        index = ord(c) - ord('a')
        if c == "#" or not node.links[index]: return
        node = node.links[index]

        if node.word:
            res.append(node.word)
            node.word = "" # de-duplicate
        
        board[i][j] = "#" # doing
        self.dfs(board, i+1, j, node, res)
        self.dfs(board, i-1, j, node, res)
        self.dfs(board, i, j+1, node, res)
        self.dfs(board, i, j-1, node, res)
        board[i][j] = c
    
    def build_trees(self, words):
        root = TrieNode()
        for word in words:
            node = root
            for c in word:
                index = ord(c) - ord('a')
                if not node.links[index]:
                    node.links[index] = TrieNode()
                node = node.links[index]
            node.word = word
        return root
    