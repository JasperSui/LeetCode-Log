class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # selection sort
        for i in range(len(nums), 0, -1):
            temp = 0
            print(i)
            for j in range(i):
                if not self.compare(nums[j], nums[temp]):
                    temp = j
            nums[temp], nums[i-1] = nums[i-1], nums[temp]
        return str(int("".join(map(str, nums))))
    
    def compare(self, n1, n2):
        return int(str(n1) + str(n2)) > int(str(n2) + str(n1))
        