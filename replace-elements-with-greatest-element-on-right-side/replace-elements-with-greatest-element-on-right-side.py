class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        m = -1
        for i in range(len(arr)-1 , -1, -1):
            arr[i], m = m, max(m, arr[i])
        return arr