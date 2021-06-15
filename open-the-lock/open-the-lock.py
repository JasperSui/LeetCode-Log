class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        def plus(s, index):
            s = list(s)
            if s[index] == '9': s[index] = '0'
            else: s[index] = str(int(s[index]) + 1)
            return ''.join(s)
        
        def minus(s, index):
            s = list(s)
            if s[index] == '0': s[index] = '9'
            else: s[index] = str(int(s[index]) - 1)
            return ''.join(s)
        
        steps = 0
        visited = set()
        deadends = set(deadends)
        queue = deque(['0000'])
        while queue:
            for i in range(len(queue)):
                curr = queue.popleft()
                if curr in deadends: continue
                if curr == target: return steps
                for i in range(4):
                    up = plus(curr, i)
                    down = minus(curr, i)
                    if up not in visited:
                        queue.append(up)
                        visited.add(up)
                    if down not in visited:
                        queue.append(down)
                        visited.add(down)
            steps += 1
        return -1
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         def plus(s, index):
#             s = list(s)
#             if s[index] == '9': s[index] = '0'
#             else: s[index] = str(int(s[index])+1)
#             return ''.join(s)
        
#         def minus(s, index):
#             s = list(s)
#             if s[index] == '0': s[index] = '9'
#             else: s[index] = str(int(s[index])-1)
#             return ''.join(s)

#         deadends = set(deadends)
#         visited = set('0000')
#         queue = deque(['0000'])
#         steps = 0
#         while queue:
#             for _ in range(len(queue)):
#                 cur = queue.popleft()
#                 if cur in deadends: continue
#                 if cur == target: return steps
#                 for i in range(4):
#                     up = plus(cur, i)
#                     down = minus(cur, i)
#                     if up not in visited:
#                         queue.append(up)
#                         visited.add(up)
#                     if down not in visited:
#                         queue.append(down)
#                         visited.add(down)
#             steps += 1
#         return -1