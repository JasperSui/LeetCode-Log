class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        nums = []
        for i, (et, pt) in enumerate(tasks):
            heapq.heappush(nums, (et, pt, i))
        tasks = nums
        waiting = []
        res = []
        while tasks or waiting:
            if waiting:
                pt, idx = heapq.heappop(waiting)
            else:
                et, pt, idx = heapq.heappop(tasks)
                finishTime = et
            finishTime += pt
            res += [idx]
            while tasks and tasks[0][0] <= finishTime:
                et, pt, idx = heapq.heappop(tasks)
                heapq.heappush(waiting, (pt, idx))

        return res