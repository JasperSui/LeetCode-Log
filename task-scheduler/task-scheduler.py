class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = defaultdict(int)
        max_count, max_tasks = 0, 0
        for c in tasks:
            d[c] += 1
            if d[c] > max_count:
                max_count = d[c]
                max_tasks = 1
            elif d[c] == max_count:
                max_tasks += 1
        
        part_count = max_count - 1
        part_len = n - (max_tasks - 1)
        empty_slots = part_count * part_len
        available_tasks = len(tasks) - max_count * max_tasks
        idles = max(0, empty_slots - available_tasks)
        return len(tasks) + idles