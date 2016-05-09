class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        n1=m
        n2=n
        i=m+n-1
        while n2>=1:
            if n1>=1:
                if nums1[n1-1]>=nums2[n2-1]:
                    nums1[i]=nums1[n1-1]
                    n1 -= 1
                    i -= 1
                else:
                    nums1[i]=nums2[n2-1]
                    n2 -= 1
                    i -= 1
            else:
                nums1[i]=nums2[n2-1]
                n2 -= 1
                i -= 1
        
        
