class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zeros = 0
        i = 0
        while i<len(nums):
            while i<len(nums) and nums[i] == 0:
                zeros += 1
                i += 1
            if i<len(nums):
                nums[i-zeros] = nums[i]
                i += 1
                print(i)
        for j in range(len(nums)-zeros, len(nums)):
            nums[j] = 0
                
