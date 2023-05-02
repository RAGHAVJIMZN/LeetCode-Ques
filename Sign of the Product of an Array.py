class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if nums.count(0) >=1:
            return 0
        # no of negative numbers in list
        count_neg = sum([1 for i in nums if i <0])
        
        if count_neg %2 == 0:
            return 1
        else:
            return -1
        