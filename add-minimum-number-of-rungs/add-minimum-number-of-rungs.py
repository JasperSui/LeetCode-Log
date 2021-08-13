class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        ans = 0
        rungs = [0] + rungs
        for i in range(1, len(rungs)):
            diff = rungs[i] - rungs[i-1]
            if diff > dist:
                if diff % dist == 0:
                    ans += diff // dist - 1
                else:
                    ans += diff // dist
        return ans