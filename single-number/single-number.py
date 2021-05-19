class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = set()
        b = set()
        for n in nums:
            if n not in a and n not in b: a.add(n)
            elif n in a and n not in b: 
                a.remove(n)
                b.add(n)
        return a.pop()