class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        sum = 0
        for i in range(len(num)):
            sum = sum*10 + num[i] 
        sum = sum + k
        lst =[]
        a = str(sum)
        for i in range(len(a)):
            lst.append(a[i])
        res = [eval(i) for i in lst]
        return res
