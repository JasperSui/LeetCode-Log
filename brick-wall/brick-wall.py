class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        sum_of_row = sum(wall[0])
        spaces = defaultdict(int)
        for row in wall:
            count = 0
            for n in row:
                count += n
                if count != sum_of_row:
                    spaces[count] += 1
        if not spaces.values(): return len(wall)
        return len(wall) - max(spaces.values())