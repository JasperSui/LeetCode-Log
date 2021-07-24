class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        arrivals = []
        departures = []
        for index, (s, e) in enumerate(times):
            heappush(arrivals, (s, index))
            heappush(departures, (e, index))
        d = {}
        occupied = [0] * len(times)
        while True:
            if arrivals and departures and arrivals[0][0] < departures[0][0]:
                _, index = heappop(arrivals)
                d[index] = occupied.index(0)
                occupied[d[index]] = 1
                if index == targetFriend:
                    return d[index]
            elif arrivals and departures and arrivals[0][0] >= departures[0][0]:
                _, index = heappop(departures)
                occupied[d[index]] = 0