class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        left = 0
        right = k-1
        sub_sum = sum(arr[i] for i in range(k))
        count = 0
        while right<len(arr):
            if sub_sum //k >= threshold:
                count+=1
            sub_sum -= arr[left]
            left+=1
            right+=1
            if right<len(arr):
                sub_sum+=arr[right]
            
            
        return count
            
            
        return count