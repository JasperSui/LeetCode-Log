class WordFreq:
    def __init__(self, word, count):
        self.word = word
        self.count = count
    
    def __lt__(self, obj):
        if self.count == obj.count:
            return self.word > obj.word
        return self.count < obj.count
    
    def __gt__(self, obj):
        return self.count > obj.count

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = Counter(words)
        pq = []
        
        for word, count in d.items():
            heapq.heappush(pq, WordFreq(word, count))
            if len(pq) > k:
                heapq.heappop(pq)
        
        res = []
        for _ in range(k):
            res.append(heapq.heappop(pq).word)
        
        return reversed(res)
            