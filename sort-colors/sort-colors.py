class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Dutch national flags problem
        red, white, blue = 0, 0, len(nums)-1
        while white <= blue:
            if nums[white] == 0: # red
                nums[red], nums[white] = nums[white], nums[red]
                white += 1
                red += 1
            elif nums[white] == 1: # white
                white += 1
            elif nums[white] == 2: # blue
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1