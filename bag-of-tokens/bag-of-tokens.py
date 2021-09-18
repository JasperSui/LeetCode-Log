class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        if not tokens: return 0
        tokens.sort()
        score = 0
        ans = score
        if power < tokens[0]: return 0
        while tokens:
            if power >= tokens[0]:
                score += 1
                power -= tokens[0]
                tokens.pop(0)
            else:
                score -= 1
                power += tokens[-1]
                tokens.pop()
            ans = max(ans, score)
        return ans