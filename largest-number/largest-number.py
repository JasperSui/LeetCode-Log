class Solution:
    
    # quick sort, in-place
    def largestNumber(self, nums: List[int]) -> str:
        self.quicksort(nums, 0, len(nums)-1)
        return str(int("".join(map(str,nums))))
    
    def quicksort(self, nums, l, r):
        if l >= r: return
        pos = self.partition(nums, l, r)
        self.quicksort(nums, l, pos-1)
        self.quicksort(nums, pos+1, r)
    
    def partition(self, nums, l, r):
        low = l
        while l < r:
            if self.compare(nums[l], nums[r]):
                nums[l], nums[low] = nums[low], nums[l]
                low += 1
            l += 1
        nums[low], nums[r] = nums[r], nums[low]
        return low
    
    def compare(self, n1, n2):
        return str(n1) + str(n2) > str(n2) + str(n1)
    
    
#     # merge sort
#     def largestNumber(self, nums: List[int]) -> str:
#         nums = self.merge_sort(nums, 0, len(nums)-1)
#         return str(int("".join(map(str, nums))))
    
#     def merge_sort(self, nums, l, r):
#         if l > r: return
#         if l == r:
#             return [nums[l]]
#         mid = l + (r-l) // 2
#         left = self.merge_sort(nums, l, mid)
#         right = self.merge_sort(nums, mid+1, r)
#         return self.merge(left, right)
    
#     def merge(self, l1, l2):
#         res, i, j = [], 0, 0
#         while i < len(l1) and j < len(l2):
#             if not self.compare(l1[i], l2[j]):
#                 res.append(l2[j])
#                 j += 1
#             else:
#                 res.append(l1[i])
#                 i += 1
#         res.extend(l1[i:] or l2[j:])
#         return res
    
#     def compare(self, n1, n2):
#         return str(n1) + str(n2) > str(n2) + str(n1)
    
#     # insertion sort
#     def largestNumber(self, nums: List[int]) -> str:
#         for i in range(len(nums)):
#             pos, curr = i, nums[i]
#             while pos > 0 and not self.compare(nums[pos-1], curr):
#                 nums[pos] = nums[pos-1]
#                 pos -= 1
#             nums[pos] = curr
#         return str(int("".join(map(str, nums))))
    
#     def compare(self, n1, n2):
#         return str(n1) + str(n2) > str(n2) + str(n1)
    
    
#     # bubble sort
#     def largestNumber(self, nums: List[int]) -> str:
#         for i in range(len(nums), 0, -1):
#             for j in range(i-1):
#                 if not self.compare(nums[j], nums[j+1]):
#                     nums[j], nums[j+1] = nums[j+1], nums[j]
#         return str(int("".join(map(str, nums))))
    
#     def compare(self, n1, n2):
#         return str(n1) + str(n2) > str(n2) + str(n1)
    
    
#     # selection sort
#     def largestNumber(self, nums: List[int]) -> str:
#         for i in range(len(nums), 0, -1):
#             temp = 0
#             for j in range(i):
#                 if not self.compare(nums[j], nums[temp]):
#                     temp = j
#             nums[temp], nums[i-1] = nums[i-1], nums[temp]
#         return str(int("".join(map(str, nums))))
    
#     def compare(self, n1, n2):
#         return int(str(n1) + str(n2)) > int(str(n2) + str(n1))
        