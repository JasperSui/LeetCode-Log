class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # # O(nlogn)
        # d = collections.Counter(nums)
        # d = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
        # return [key for key in list(d.keys())[:k]]
        
        # O(n)
        bucket_list = [[] for _ in range(len(nums) + 1)]
        d = Counter(nums)
        for key, freq in d.items():
            bucket_list[freq].append(key)
        
        res = []
        for i in range(len(bucket_list)-1, -1, -1):
            bucket = bucket_list[i]
            if bucket:
                for key in bucket:
                    res.append(key)
                    if len(res) == k:
                        return res