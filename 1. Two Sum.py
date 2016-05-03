#Same mistake as Java
#No sorting!!!
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sorted(nums)
        j = len(nums)-1
        i=0
        while(i<j):
            if nums[i]+nums[j]==target:
                return [i,j]
            elif nums[i]+nums[j]<target:
                i +=1
            elif nums[i]+nums[j]>target:
                j -=1
        return null
            

#Use dictionary (hashtable in java), number as key, position as value
#Correst solution 1 -- use xrange
class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        dict = {}
        for i in xrange(len(num)):
            x = num[i]
            if target-x in dict:
                return (dict[target-x]+1, i+1)
            dict[x] = i

#Correst solution 2 -- use range
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        temp_dict = {}
        for i in range(len(nums)):
            if nums[i] in temp_dict:
                return [temp_dict[nums[i]], i]
            temp_dict[target-nums[i]] = i
            
            
