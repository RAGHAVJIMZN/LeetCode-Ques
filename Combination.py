class Solution(object):
    def do_combine(self, nums, k, prefix, answer):
        
        if not k:
            answer.append(prefix)
        
        if len(nums) >=k:
            for i, num in enumerate(nums):
                self.do_combine(nums[i+1:], k-1, prefix+[num], answer)
        
        return answer
    
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        return self.do_combine(range(1,n+1), k , [], [])