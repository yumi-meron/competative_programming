class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m-1
        j=n-1
        ind = n+m-1
        while j>=0:
            if i>=0 and nums2[j]<nums1[i]:
                nums1[ind] = nums1[i]
                i-=1
            else:
                nums1[ind] = nums2[j]
                j-=1
            ind-=1
            
            
            
        
            
            
            
                