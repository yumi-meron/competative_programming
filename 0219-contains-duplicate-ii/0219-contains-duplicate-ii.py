class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        left=0
        subset = set()
        for i in range(len(nums)):
            if nums[i] in subset and abs(left-i)<=k:
                return True
            subset.add(nums[i])
            if len(subset)>k:
                subset.remove(nums[left])
                left+=1
                
        return False
                