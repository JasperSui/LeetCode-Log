class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = defaultdict(int)
        ma = 0
        max_count = 0
        for c in tasks:
            index = ord(c) - ord('A')
            d[index] += 1
            if d[index] > ma:
                ma = d[index]
                max_count = 1
            elif d[index] == ma:
                max_count += 1
        
        part_count = ma - 1
        part_len = n - (max_count - 1)
        empty_slots = part_count * part_len
        available_tasks = len(tasks) - (ma * max_count)
        idles = max(0, empty_slots - available_tasks)
        return len(tasks) + idles