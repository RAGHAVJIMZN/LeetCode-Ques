class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        ar1 = []
        j = 1 
        for i in range(1 ,arr[-1]+2*k):
            ar1.append(j)
            j += 1 
        for n in range(1, len(ar1)) :
            if n in arr :
                ar1.remove(n)
        return ar1[k-1]