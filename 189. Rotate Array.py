#My wrong solution
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        while k>=len(nums):
            k=k-len(nums)
        temp=nums[:len(nums)-k]
        for i in range(len(nums)-k,len(nums)):
            nums[i-k]=nums[i] #这里不对，因为i可能小于k
        for j in range(0,len(nums)-k):
            nums[j+k] = temp[j]
            

#Correct Solution-1
#time complexity-O(n), space complexity-O(1)
class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k):
        n = len(nums)
        k %= n
        self.reverse(nums, 0, n - k)
        self.reverse(nums, n - k, n)
        self.reverse(nums, 0, n)

    def reverse(self, nums, start, end):
        for x in range(start, (start + end) / 2):
            nums[x] ^= nums[start + end - x - 1]
            nums[start + end - x - 1] ^= nums[x]
            nums[x] ^= nums[start + end - x - 1]
            
#Correct Solution-2
#time complexity-O(n), space complexity-O(1)
class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k):
        n = len(nums)
        idx = 0
        distance = 0
        cur = nums[0]
        for x in range(n):
            idx = (idx + k) % n
            nums[idx], cur = cur, nums[idx]
            
            distance = (distance + k) % n
            if distance == 0:
                idx = (idx + 1) % n
                cur = nums[idx]
  
#Correct Solution-3
#time complexity-O(n), space complexity-O(n)
class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k):
        n = len(nums)
        if k > 0 and n > 1:
            nums[:] = nums[n - k:] + nums[:n - k]
