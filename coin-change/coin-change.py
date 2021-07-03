class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        stack1 = {0}
        stack2 = set()
        visited = [False]*(amount+1)
        visited[0] = [True]
        ans = 0
        while stack1:
            ans += 1
            for x in stack1:
                for y in coins:
                    new = x + y
                    if new == amount:
                        return ans
                    elif new >= amount:
                        continue
                    elif not visited[new]:
                        visited[new] = True
                        stack2.add(new)
            stack1, stack2 = stack2, set()
        return -1