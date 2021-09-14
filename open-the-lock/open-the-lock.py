class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def plus(s, index):
            s = list(s)
            if s[index] == '9':
                s[index] = '0'
            else:
                s[index] = str(int(s[index])+1)
            return "".join(s)

        def minus(s, index):
            s = list(s)
            if s[index] == '0':
                s[index] = '9'
            else:
                s[index] = str(int(s[index])-1)
            return "".join(s)
        
        queue = deque([('0000', 0)])
        deadends = set(deadends)
        visited = set()
        while queue:
            s, steps = queue.popleft()
            if s == target: return steps
            if s in deadends: continue
            if s in visited: continue
            visited.add(s)
            for i in range(4):
                queue.append((plus(s, i), steps+1))
                queue.append((minus(s, i), steps+1))
        return -1