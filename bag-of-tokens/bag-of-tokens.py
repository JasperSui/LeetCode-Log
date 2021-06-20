class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        score = 0
        max_score = 0
        if not tokens or min(tokens) > power: return score
        tokens.sort()
        tokens = deque(tokens)
        while tokens:
            if score == 0:
                if tokens[0] <= power:
                    power -= tokens.popleft()
                    score += 1
                    max_score = max(max_score, score)
                else:
                    return max_score
            else:
                if tokens[0] <= power:
                    power -= tokens.popleft()
                    score += 1
                    max_score = max(max_score, score)
                else:
                    power += tokens.pop()
                    score -= 1
        return max_score