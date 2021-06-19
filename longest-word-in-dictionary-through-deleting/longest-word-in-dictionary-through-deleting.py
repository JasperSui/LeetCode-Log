class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        def isSubSequence(x):
            it = iter(s)
            return all(c in it for c in x)
        return min(list(filter(isSubSequence, dictionary)) + [''], key= lambda x: (-len(x), x))