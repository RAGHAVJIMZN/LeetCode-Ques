class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return -1
        Lbounder, Rbounder, mid = 0, len(nums), len(nums)//2
        while Rbounder!=Lbounder:
            if target > nums[mid]:
                Lbounder = mid
                mid += (Rbounder-Lbounder)//2
            elif target < nums[mid]:
                Rbounder = mid
                mid = (Rbounder-Lbounder)//2
            else:
                return mid
        return mid

        