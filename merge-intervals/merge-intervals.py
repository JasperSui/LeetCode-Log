class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        stack = []
        for s, e in sorted(intervals, key=lambda x: x[0]):
            if stack and stack[-1][1] >= s:
                stack[-1][1] = max(stack[-1][1], e)
            else:
                stack.append([s, e])
        return stack
        
        
        
        # curr = 0
        # intervals.sort(key=lambda x: x[0])
        # while curr < len(intervals)-1:
        #     curr_1, curr_2 = intervals[curr]
        #     next_1, next_2 = intervals[curr+1]
        #     if curr_2 >= next_1:
        #         intervals[curr] = [min(curr_1, next_1), max(curr_2, next_2)]
        #         del intervals[curr+1]
        #     else:
        #         curr += 1
        # return intervals
        
        # out = []
        # for start, end in sorted(intervals, key=lambda x: x[0]):
        #     if out and start <= out[-1][1]:
        #         out[-1][1] = max(out[-1][1], end)
        #     else:
        #         out += [[start, end]]
        # return out
    
        # out = []
        # for i in sorted(intervals, key=lambda x: x[0]):
        #     if out and i[0] <= out[-1][1]:
        #         out[-1][1] = max(out[-1][1], i[1])
        #     else:
        #         out += [i]
        # return out