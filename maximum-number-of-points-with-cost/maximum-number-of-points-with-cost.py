class Solution:
    def maxPoints(self, P: List[List[int]]) -> int:
        m = len(P)
        n = len(P[0])
        if m == 1: return max(P[0])
        if n == 1: return sum([li[0] for li in P])
        
        def get_left(li):
            left = [li[0]] + [0] * (n-1)
            for i in range(1, n):
                left[i] = max(li[i], left[i-1] - 1)
            return left
        
        def get_right(li):
            right = [0] * (n-1) + [li[-1]]
            for i in range(n-2, -1, -1):
                right[i] = max(li[i], right[i+1] - 1)
            return right
        
        pre = P[0]
        for i in range(m-1):
            left = get_left(pre)
            right = get_right(pre)
            curr = [0] * n
            for j in range(n):
                curr[j] = P[i+1][j] + max(left[j], right[j])
            pre = curr.copy()
        return max(pre)