# we have to convert string containing roman to integer
# only trick of this question to handle situation when string is like
# "IV" = 4 , "IX = 9 

roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
class Solution:
    def romanToInt(self, s: str) -> int:
        values = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        sum = 0 
        # for all character except last one 
        for i in range(len(s)-1):
                if values[s[i+1]] > values[s[i]]:
                    sum = sum - values[s[i]]
                else :
                    sum = sum + values [s[i]]
        # for last character 
        sum = sum + values[s[len(s)-1]]

        return sum 