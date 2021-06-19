class Solution:
    def reorganizeString(self, s: str) -> str:
        res = []
        d = collections.Counter(s)
        keys = set(d.keys())
        last = None
        while len(res) != len(s):
            c, _ = max(d.items(), key=lambda x: x[1])
            if last != c:
                res.append(c)
                d[c] -= 1
                last = c
            else:
                max_char, max_count = "", 0
                for char in keys - set(c):
                    if d[char] > max_count:
                        max_count = d[char]
                        max_char = char
                if max_count == 0: return ""
                res.append(max_char)
                d[max_char] -= 1
                last = max_char
        return "".join(res)