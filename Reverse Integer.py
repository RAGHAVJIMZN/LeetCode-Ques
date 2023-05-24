class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0 :
            x = int(str(x)[::-1]) 
        else :
            x = abs(x)
            x = int(str(x)[::-1])
            x = 0 - x
        return x if abs(x) < 2147483648 else 0