class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        brick_len = sum(wall[0])
        space = defaultdict(int)
        for row in wall:
            count = 0
            for num in row:
                count += num
                if count < brick_len:
                    space[count] += 1
                    
        if not space.values(): return len(wall)
        return len(wall) - max(space.values())