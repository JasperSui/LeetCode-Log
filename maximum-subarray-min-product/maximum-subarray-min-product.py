class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        n = len(nums)
        left_bound, right_bound = [0] * (n), [0] * (n)
        st = []
        for i in range(n):
            while st and nums[st[-1]] >= nums[i]: st.pop()
            if st:
                left_bound[i] = st[-1] + 1
            else:
                left_bound[i] = 0
            st.append(i)
        
        st = []
        for i in reversed(range(n)):
            while st and nums[st[-1]] >= nums[i]: st.pop()
            if st:
                right_bound[i] = st[-1] - 1
            else:
                right_bound[i] = n - 1
            st.append(i)
        
        presum = [0] * (n+1)
        for i in range(n):
            presum[i+1] = presum[i] + nums[i]
        
        def get_sum(left, right):
            return presum[right+1] - presum[left]
        
        ma = 0
        for i in range(n):
            ma = max(ma, nums[i] * get_sum(left_bound[i], right_bound[i]))
        
        return ma % (10 ** 9 + 7)