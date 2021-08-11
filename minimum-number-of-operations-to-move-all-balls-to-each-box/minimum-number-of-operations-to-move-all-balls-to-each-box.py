class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        res = [0] * n
        curr, step = 0, 0
        for i in range(n):
            res[i] += step
            curr += int(boxes[i])
            step += curr
        
        curr, step = 0, 0
        for i in reversed(range(n)):
            res[i] += step
            curr += int(boxes[i])
            step += curr
        return res