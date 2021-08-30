class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Moyer vote method
        major = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if count == 0: # means there is no major in the "FRONT"
                count += 1
                major = nums[i]
            elif nums[i] == major:
                count += 1
            else:
                count -= 1
        return major