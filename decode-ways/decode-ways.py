class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0': return 0
        
        dp = [0 for x in range(len(s) + 1)]
        dp[0:2] = [1, 1]
        
        for i in range(2, len(s) + 1):
            if 0 < int(s[i-1:i]):
                dp[i] += dp[i-1]
            if 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]
        return dp[-1]
        
        # if not s or s[0] == '0': return 0
        # carry = 0
        # res = []
        # for i in s:
        #     i = int(i)
        #     if not carry and i <= 2:
        #         carry = i
        #     elif not carry:
        #         res.append(i)
        #     elif carry and i <= 6:
        #         res.append(carry*10+i)
        #         carry = 0
        #     elif carry:
        #         res.append(carry)
        #         res.append(i)
        #         carry = 0
        # ans = 0
        # print(res)
        # for n in res:
        #     if n > 10 and n % 10:
        #         ans += 2
        #     else:
        #         ans += 1
        # return ans