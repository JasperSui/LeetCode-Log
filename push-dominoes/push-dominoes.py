class Solution:
    def pushDominoes(self, d: str) -> str:
        d = "L" + d + "R"
        res = ""
        i = 0
        for j in range(1, len(d)):
            if d[j] == ".":
                continue
            if i:
                res += d[i]
                
            mid = j - i - 1
            if d[i] == d[j]:
                res += d[i] * mid
            
            elif d[j] == "R" and d[i] == "L":
                res += "." * mid
            
            else:
                res += "R" * (mid // 2) + "." * (mid % 2) + "L" * (mid // 2)
            i = j
        return res
            