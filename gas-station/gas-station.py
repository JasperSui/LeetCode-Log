class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tank = 0
        start = 0
        sum_gas, sum_cost = 0, 0
        for i in range(len(gas)):
            sum_gas += gas[i]
            sum_cost += cost[i]
            tank += gas[i] - cost[i]
            if tank < 0:
                start = i + 1
                tank = 0
        return start if sum_gas - sum_cost >= 0 else -1
            
            