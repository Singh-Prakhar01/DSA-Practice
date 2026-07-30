# Last updated: 30/07/2026, 23:26:15
1class Solution:
2    def removeDuplicates(self, nums: List[int]) -> int:
3        if len(nums) <= 2:
4            return len(nums)
5
6        k = 2  # First two elements are always allowed
7
8        for i in range(2, len(nums)):
9            if nums[i] != nums[k - 2]:
10                nums[k] = nums[i]
11                k += 1
12
13        return k
14        