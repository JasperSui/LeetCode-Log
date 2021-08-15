class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        queue = deque([[start, start, 0]])
        
        while queue:
            curr, prev, steps = queue.popleft()
            if curr == end:
                return steps
            for avaiable_gene in bank:
                if self.is_changable(curr, avaiable_gene) and prev != avaiable_gene:
                    queue.append([avaiable_gene, curr, steps+1])
        return -1
    
    def is_changable(self, a, b):
        diff = 0
        for i in range(len(a)):
            if a[i] != b[i]: diff += 1
        return diff == 1
        