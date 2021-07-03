class Solution:
    def numSquares(self, n: int) -> int:
        if n < 2: return n
        squares = []
        i = 1
        while i*i <= n:
            squares.append(i*i)
            i += 1
        
        ans = 0
        stack = {n}
        while stack:
            temp = set()
            ans += 1
            for i in stack:
                for square in squares:
                    if i == square:
                        return ans
                    if i < square:
                        break
                    temp.add(i-square)
            stack = temp
        return ans