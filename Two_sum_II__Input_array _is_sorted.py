class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lst = []
        lth = len(numbers)
        low , high = 0 , lth - 1
        sum = numbers[low] + numbers[high]
        while(sum != target):
            if(sum < target) :
                low += 1
            else :
                high-= 1
            sum = numbers[low] + numbers[high]
        lst.append(low+1)
        lst.append(high+1)
        return lst