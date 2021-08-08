class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        rightmost = {char: index for index, char in enumerate(s)}
        left, right = 0, 0
        res = []
        for index, char in enumerate(s):
            right = max(right, rightmost[char])
            if index == right:
                res.append(right - left + 1)
                left = index + 1
        return res
            
        