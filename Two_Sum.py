# nums = [2,7,11,15]
# target = 9
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lst = []
        for i in range(len(nums)):
            a = nums[i]
            one = i 
            for j in range(i+1,len(nums)):
                b = nums[j]
                two = j 
                if (a+b) == target:
                    lst.append(one)
                    lst.append(two)
        return lst
    