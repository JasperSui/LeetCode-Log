class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need, window = defaultdict(int), defaultdict(int)
        for c in t:
            need[c] += 1
        
        left, right, valid = 0, 0, 0
        start, start_len = 0, float('inf')
        cur = ""

        while right < len(s):
            c = s[right]
            right += 1
            if c in need:
                window[c] += 1
                
                # window 裡的 c 的數量和 need 一樣 (滿足條件)
                if window[c] == need[c]: valid += 1
            
            while valid == len(need):
                if (right - left < start_len):
                    start = left
                    start_len = right - left
                d = s[left]
                left += 1
                if d in need:
                    if window[d] == need[d]: valid -= 1
                    window[d] -= 1
        if start_len == float('inf'): return ""
        else: return s[start:start+start_len]