def check(n):
        count =  0 
        for i in bin(n):
            if i == "1":
                count += 1 
        return count 
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 0 :
            return False 
        else :
            ans = check(n)
            if ans == 1 :
                return True 
            else :
                return False 



