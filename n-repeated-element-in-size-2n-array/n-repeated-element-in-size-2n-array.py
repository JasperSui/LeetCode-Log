class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        l = [0] * (max(A)+1)
        for n in A:
            if l[n] == 1: return n
            l[n] += 1
        # B = set(A)
        # return int((sum(A)-sum(B)) // ((len(A) /2) -1))