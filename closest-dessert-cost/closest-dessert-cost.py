class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        baseCosts.sort(reverse=True)
        toppingCosts.sort(reverse=True)
        res = baseCosts[0]
        res_delta = abs(target - res)
        for bc in baseCosts:
            candidates = set([bc])
            for tc in toppingCosts:
                new_candidates = set()
                for c in candidates:
                    for x in range(3):
                        nc = c + x*tc
                        if nc - target < res_delta:
                            new_candidates.add(nc)
                        delta = abs(nc - target)
                        if delta < res_delta or (delta == res_delta and nc < res):
                            res = nc
                            res_delta = delta
                candidates = new_candidates
        return res
                        