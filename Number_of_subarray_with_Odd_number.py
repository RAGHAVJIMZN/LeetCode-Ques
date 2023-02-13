# we have high two interger low and high 
# we have to find odd number between them including them

class Solution:
    def countOdds(self, low: int, high: int) -> int:

        if low % 2 == 1 or high % 2 == 1:
            return (high - low) // 2 + 1
        else:
            return (high - low)//2
