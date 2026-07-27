# Last updated: 27/07/2026, 15:21:05
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        size =len(numbers)
        i = 0 
        j = size-1
        while i<j:
            s = numbers[i] + numbers[j]
            if s > target :
                j -= 1
            elif  s < target :
                i += 1
            else :
                return [i+1,j+1]
        return [-1,-1]
        