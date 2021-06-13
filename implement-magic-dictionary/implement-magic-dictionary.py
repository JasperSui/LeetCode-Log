class MagicDictionary:
    
    def _candidates(self, word):
        for i in range(len(word)):
            yield word[:i] + "*" + word[i+1:]

    def buildDict(self, dictionary: List[str]) -> None:
        self.words = set(dictionary)
        self.near = collections.Counter(cand for word in self.words for cand in self._candidates(word))

    def search(self, searchWord: str) -> bool:
        return any(self.near[cand] > 1 or self.near[cand] == 1 and searchWord not in self.words for cand in self._candidates(searchWord))

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)