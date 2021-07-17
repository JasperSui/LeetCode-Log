class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = defaultdict(int)
        ma = 0
        max_count = 0
        for c in tasks:
            d[ord(c) - ord("A")] += 1
            if d[ord(c) - ord("A")] > ma:
                ma = d[ord(c) - ord("A")]
                max_count = 1
            elif d[ord(c) - ord("A")] == ma:
                max_count += 1
        
        part_count = ma - 1
        part_len = n - (max_count - 1)
        empty_slots = part_count * part_len
        available_tasks = len(tasks) - ma * max_count
        idles = max(0, empty_slots - available_tasks)
        return len(tasks) + idles