class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            '1': '',
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
            '0': ' '}
        res = [''] if digits else []
        for d in digits:
            temp = []
            for q in mapping[d]:
                for p in res:
                    temp.append(p+q)
            res = temp
        return res