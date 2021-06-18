class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        low, high = 0, len(A)-1
        while low <= high:
            if A[low] % 2 == 0:
                low += 1
            else:
                A[low], A[high] = A[high], A[low]
                high -= 1
        return A        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # s, e = 0, len(A) - 1
        # while s <= e:
        #     if A[s] % 2 == 0: s += 1
        #     else:
        #         A[s], A[e] = A[e], A[s]
        #         e -= 1
        # return A