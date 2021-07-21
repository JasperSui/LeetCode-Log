class Solution:
    def frequencySort(self, s: str) -> str:
        buckets = [[] for _ in range(len(s)+1)]
        d = Counter(s[::-1])
        for k, v in d.items():
            buckets[v].append(k)
        
        res = ""
        for i in range(len(s), -1, -1):
            if buckets[i]:
                for c in buckets[i]:
                    res += c * i
        return res