class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary = set(dictionary)
        ans = []
        sentences = sentence.split()
        for s in sentences:
            added = False
            for i in range(len(s)):
                if s[:i] in dictionary:
                    ans.append(s[:i])
                    added = True
                    break
            
            if not added:
                ans.append(s)
        return " ".join(ans)