class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        mutated = False
        nums = list(map(int, num))
        for i in range(len(num)):
            d = int(num[i])
            nums[i] = max(d, change[d])
            if change[d] < d and mutated:
                break
            mutated |= change[d] > d
        return "".join(map(str,nums))
        