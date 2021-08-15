class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        A = deque(sorted(A))
        for b, i in sorted([[b, i] for i, b in enumerate(B)], reverse=True):
            B[i] = A.pop() if b < A[-1] else A.popleft()
        return B