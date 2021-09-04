class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = Counter(nums)
        bucket_list = [set() for _ in range(len(nums)+1)]
        for key, freq in d.items():
            bucket_list[freq].add(key)
        
        res = []
        for i in range(len(nums), -1, -1):
            bucket = bucket_list[i]
            if bucket:
                for n in bucket:
                    res.append(n)
                    if len(res) == k:
                        return res