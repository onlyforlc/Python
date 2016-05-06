class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        numDict = {}
        for i in range(len(nums)):
            if numDict.get(nums[i])>=0:
                return True;
            else:
                numDict[nums[i]] = i
        return False;
