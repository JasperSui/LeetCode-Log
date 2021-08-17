class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            "1": "",
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        res = ['']
        if not digits: return []
        for d in digits:
            temp = []
            for p in res:
                for q in mapping[d]:
                    temp.append(p+q)
            res = temp
        return res