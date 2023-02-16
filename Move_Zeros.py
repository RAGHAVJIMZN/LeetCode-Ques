class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = nums.count(0)
        for i in range(k):
            nums.remove(0)
        for i in range(k):
            nums += [0]