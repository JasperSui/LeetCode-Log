class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        d = "L" + dominoes + "R"
        res = ""
        i = 0
        
        for j in range(1, len(d)):
            if d[j] == ".":
                continue
            
            if i:
                res += d[i]
            
            space = j - i - 1
            if d[i] == d[j]:
                res += d[i] * space
            
            elif d[i] == "L" and d[j] == "R":
                res += "." * space
            
            else:
                res += "R" * (space // 2) + "." * (space % 2) + "L" * (space // 2)
            
            i = j
        return res