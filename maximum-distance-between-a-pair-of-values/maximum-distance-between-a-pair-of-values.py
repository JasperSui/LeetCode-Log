class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i = j = ans = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                i += 1
            else:
                ans = max(ans, j-i)
                j += 1
                
        return ans