class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        temp = [s[i:i+10] for i in range(len(s)-9)]
        return [k for k, v in collections.Counter(temp).items() if v >= 2]
            