# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n):
        if n < 2:
            if isBadVersion(n):
                return n
            return -1
        low, high = 1, n
        first_bad_version = None
        while low < high:
            mid = (low + high) // 2
            if isBadVersion(mid) is True:
                first_bad_version = mid
                high = mid
            else:
                low = mid + 1
        if isBadVersion(low) and low != first_bad_version:
                return low
        return first_bad_version