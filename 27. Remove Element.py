# My solution -- slow -- O(N^2)
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = nums.count(val)
        for x in range(0,count):
            nums.remove(val)
            
        return len(nums)
        

# Better -- O(N)
class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    # clrs qsort
    def removeElement(self, A, elem):
        j = len(A)-1
        for i in range(len(A) - 1, -1, -1):
            if A[i] == elem:
                A[i], A[j] = A[j], A[i]
                j -= 1
        return j+1
