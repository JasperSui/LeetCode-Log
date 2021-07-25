class Solution:
    def maximumNumber(self, num_str: str, change: List[int]) -> str:
        mutated = False
        nums = list(map(int, num_str))
        for i in range(len(num_str)):
            d = int(num_str[i])
            nums[i] = max(d, change[d])
            if change[d] < d and mutated:
                break
            mutated |= change[d] > d
        return "".join(map(str, nums))

#         res = ""
#         change_or_not = [None] * len(num_str)
#         for i, c in enumerate(num_str):
#             num = int(c)
#             if num < change[num]:
#                 change_or_not[i] = True
#             else:
#                 change_or_not[i] = False
#         d = False
#         first_index = float('-inf')
#         for i, c in enumerate(change_or_not):
#             if c:
#                 first_index = i
#                 break
#         if first_index == float('-inf'): return num_str
        
#         for i in range(first_index):
#             res += num_str[i]
#         print(change_or_not)
#         for i, c in enumerate(change_or_not[first_index:], first_index):
#             if not c or d:
#                 if not c and (not num_str[i] == str(change[int(num_str[i])])): 
#                     d = True
#                 res += num_str[i]
#             else:
#                 res += str(change[int(num_str[i])])
        
#         return res