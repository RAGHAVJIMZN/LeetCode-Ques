class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # for i in range(len(nums)):
        #     a = nums[i]
        #     c = nums.count(a)
        #     if c == 1 :
        #         return a 

        l = 0
        r = len(nums) - 1

        while l < r:
            m = (l + r) // 2
            if m % 2 == 1:
                m -= 1
            if nums[m] == nums[m + 1]:
                l = m + 2
            else:
                r = m

        return nums[l]