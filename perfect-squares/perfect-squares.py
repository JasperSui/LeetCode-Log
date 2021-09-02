class Solution:
    def numSquares(self, n: int) -> int:
        if n <= 2: return n
        choices = []
        i = 1
        while i * i <= n:
            choices.append(i*i)
            i += 1
        
        ans = 0
        stack = {n}
        while stack:
            new_stack = set()
            ans += 1
            for i in stack:
                for square in choices:
                    if square == i:
                        return ans
                    if i < square:
                        break
                    new_stack.add(i-square)
            stack = new_stack