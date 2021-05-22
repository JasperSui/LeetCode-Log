class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        self.ans = float('inf')
        toppingCosts.sort()
        for base in baseCosts:
            self.dfs(toppingCosts, target, base)
        return self.ans
    
    def dfs(self, topping, target, sums):
        if abs(target - sums) < abs(target - self.ans):
            self.ans = sums
        elif abs(target - sums) == abs(target - self.ans):
            self.ans = min(self.ans, sums)
        if sums > target: return
        if sums == target:
            self.ans = sums
            return
        for i in range(len(topping)):
            self.dfs(topping[i+1:], target, sums+0*topping[i])
            self.dfs(topping[i+1:], target, sums+1*topping[i])
            self.dfs(topping[i+1:], target, sums+2*topping[i])