class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 :
            return False 
        sum = 0 
        no = x 
        while x != 0 :
            sum = ( sum * 10 ) + x % 10
            x = x//10
        
        if no == sum :
            return True
        else :
            return False

       