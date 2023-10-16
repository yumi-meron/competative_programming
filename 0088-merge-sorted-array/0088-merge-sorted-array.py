class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = j = 0
        while i<(n+m) and j<n:
            if i >=j+m:
                nums1.insert(i,nums2[j])
                nums1.pop()
                i+=1
                j+=1
            else:
                if nums1[i]>=nums2[j]:
                    nums1.insert(i,nums2[j])
                    nums1.pop()
                    j+=1
                    i+=1
                else:
                    i+=1
            
        
            
            
            
                