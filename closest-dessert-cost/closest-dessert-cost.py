class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        baseCosts.sort(reverse=True)
        toppingCosts.sort(reverse=True)
        
        res = baseCosts[0]
        
        res_diff = abs(target - res)
        
        for bc in baseCosts:
            candidates = set([bc])
            for tc in toppingCosts:
                new_candidates = set()
                for c in candidates:
                    for times in range(3):
                        nc = c + tc * times
                        if nc - target < res_diff:
                            new_candidates.add(nc)
                        elif nc == target: return nc
                        diff = abs(nc - target)
                        if diff < res_diff or (diff == res_diff and nc < res):
                            res = nc
                            res_diff = diff
                candidates = new_candidates
        return res