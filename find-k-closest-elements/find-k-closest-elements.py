class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if x < min(arr): return arr[:k]
        elif x > max(arr): return arr[-k:]
        
        left, right = 0, len(arr) - k
        while left < right:
            mid = left + (right - left) // 2
            if x - arr[mid] > arr[mid+k] - x:
                left = mid + 1
            else:
                right = mid
        return arr[left:left+k]
        