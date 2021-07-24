class TrieNode:
    def __init__(self):
        self.links = [None] * 26
        self.is_finished = False
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr = self.root
        for c in word:
            index = ord(c) - ord('a')
            if not curr.links[index]:
                curr.links[index] = TrieNode()
            curr = curr.links[index]
        curr.is_finished = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr = self.root
        for c in word:
            index = ord(c) - ord('a')
            if not curr.links[index]: return False
            curr = curr.links[index]
        return curr.is_finished
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr = self.root
        for c in prefix:
            index = ord(c) - ord('a')
            if not curr.links[index]: return False
            curr = curr.links[index]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)