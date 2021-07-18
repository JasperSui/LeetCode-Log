class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_index, p_index, match_index, star_index = 0, 0, 0, -1
        while s_index < len(s):
            if p_index < len(p) and (s[s_index] == p[p_index] or p[p_index] == "?"):
                s_index += 1
                p_index += 1
            elif p_index < len(p) and p[p_index] == "*":
                match_index = s_index
                star_index = p_index
                p_index += 1
            elif star_index != -1:
                p_index = star_index + 1
                match_index += 1
                s_index = match_index
            else:
                return False
        while p_index < len(p) and p[p_index] == "*":
            p_index += 1
        
        if p_index == len(p):
            return True
        else:
            return False
                