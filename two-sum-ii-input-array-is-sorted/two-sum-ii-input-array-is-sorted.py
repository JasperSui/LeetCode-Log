class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers) < 2: return []
        l, r= 0, -1
        while l >= r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l+1, len(numbers)+r+1]
            elif s > target: r-=1
            elif s < target: l+=1