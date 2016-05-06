#my solution doesn't work
#has_key是python3才有的功能
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        num_dict={}
        for i in range(len(nums)):
            if(num_dict.has_key(nums[i])):
                if(abs((num_dict[nums[i]])-i)<=k):
                    return True
            else:
                num_dict[nums[i]]=i
        return False
        
#同样思路，但是可行的
class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        numDict = dict()
        for x in range(len(nums)):
            idx = numDict.get(nums[x])
            if idx >= 0 and x - idx <= k:
                return True
            numDict[nums[x]] = x
        return False
        
