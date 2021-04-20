class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        qq = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        result = []
        for word in words:
            temp = ''
            for i in list(word):
                temp += qq[ord(i)-97]
            result.append(temp)
        return len(set(result))