class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        res = [0] * len(boxes)
        indexes = set([i for i, v in enumerate(list(boxes)) if v == "1"])
        for i in range(len(boxes)):
            res[i] = sum(abs(i-j) for j in indexes)
        return res