# Last updated: 27/07/2026, 15:49:12
1class Solution:
2    def moveZeroes(self, nums: List[int]) -> None:
3        """
4        Do not return anything, modify nums in-place instead.
5        """
6        start =0 
7        n = len(nums)
8
9        for i in range (n):
10            if nums[i] != 0 :
11                nums[i],nums[start] = nums[start],nums[i]
12                start +=1