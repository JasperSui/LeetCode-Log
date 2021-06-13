class Solution:
    def frequencySort(self, s: str) -> str:
        c = sorted(collections.Counter(s).items(), key=lambda x: x[1], reverse=True)
        res = ""
        for char, times in c:
            res += char * times
        return res