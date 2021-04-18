class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greatest = {}
        stack = []
        
        for n in nums2:
            while stack and stack[-1] < n:next_greatest[stack.pop()] = n
            stack.append(n)

        for i in range(len(nums1)):
            nums1[i] = next_greatest.get(nums1[i], -1)
            
        return nums1
            