class Solution:
    def frequencySort(self, s: str) -> str:
        bucket_list = [set() for _ in range(len(s)+1)]
        d = Counter(s)
        for char, freq in d.items():
            bucket_list[freq].add(char)
        
        res = ""
        for i in range(len(bucket_list)-1, -1, -1):
            if bucket_list[i]:
                for char in bucket_list[i]:
                    res += i * char
        return res
        