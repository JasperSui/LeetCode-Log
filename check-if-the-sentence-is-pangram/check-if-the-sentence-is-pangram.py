class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        all_alphabet = set(chr(i) for i in range(97, 97+26))
        for c in sentence:
            all_alphabet.discard(c)
        return not all_alphabet