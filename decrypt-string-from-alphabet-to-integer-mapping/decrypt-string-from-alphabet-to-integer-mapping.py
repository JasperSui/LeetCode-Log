class Solution:
    def freqAlphabets(self, s: str) -> str:
        res = []
        s = deque(list(s))
        while s:
            if s[0] in ('1', '2') and len(s) >= 3 and s[2] == '#':
                res.append(f"{chr(96+int(s[0]+s[1]))}")
                for _ in range(3): s.popleft()
            else:
                res.append(f"{chr(96+int(s[0]))}")
                s.popleft()
        return "".join(res)