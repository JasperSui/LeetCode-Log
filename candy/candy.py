class Solution:
    def candy(self, ratings: List[int]) -> int:
        cookies = [1] * len(ratings)
        for i in range(len(ratings)-1):
            if ratings[i+1] > ratings[i]:
                cookies[i+1] = cookies[i] + 1
        for i in range(len(ratings)-1, 0, -1):
            if ratings[i-1] > ratings[i]:
                cookies[i-1] = max(cookies[i] + 1, cookies[i-1])
        return sum(cookies)