class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod =  1
        sum = 0 
        while n > 0 :
            s = n % 10 
            prod = prod * s 
            sum = sum + s
            n = int(n/10)
        return prod - sum