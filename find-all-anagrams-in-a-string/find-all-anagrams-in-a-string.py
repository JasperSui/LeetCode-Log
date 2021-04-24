class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        need, window = defaultdict(int), defaultdict(int)
        for c in p: need[c] += 1
        left, right, valid = 0, 0, 0
        ans = []
        while right < len(s):
            c = s[right]
            right += 1
            if c in need:
                window[c] += 1
                if need[c] == window[c]: valid += 1
            
            while right - left >= len(p):
                if valid == len(need): ans.append(left)
                d = s[left]
                left += 1
                if d in need:
                    if need[d] == window[d]: valid -= 1
                    window[d] -= 1
        return ans