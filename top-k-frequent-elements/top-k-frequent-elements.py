class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for n in nums: d[n] += 1
        return [k for k, _ in sorted(d.items(), key=lambda x: x[1], reverse=True)][:k]