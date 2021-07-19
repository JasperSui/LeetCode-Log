class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = collections.Counter(nums)
        d = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
        return [key for key in list(d.keys())[:k]]