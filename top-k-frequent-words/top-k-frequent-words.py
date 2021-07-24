class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # Brute force: O(nlogn)
        d = list(Counter(words).items())
        d.sort(key=lambda x: (-x[1], x[0]))
        return [d[0] for d in d[:k]]
        
    