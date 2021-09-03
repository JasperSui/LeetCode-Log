class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        stack = {0}
        visited = [False] * (amount + 1)
        visited[0] = True
        ans = 0
        while stack:
            new_stack = set()
            ans += 1
            for i in stack:
                for j in coins:
                    new_amount = i + j
                    if new_amount == amount: return ans
                    elif new_amount > amount: continue
                    elif not visited[new_amount]:
                        visited[new_amount] = True
                        new_stack.add(new_amount)
            stack = new_stack
        return -1