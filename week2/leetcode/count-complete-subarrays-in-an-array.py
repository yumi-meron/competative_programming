class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        distinct_elements = len(set(nums))
        left = 0
        right = 0
        counter = Counter()
        count = 0
        while right < n:
            counter[nums[right]] += 1
            while len(counter) == distinct_elements:
                count += n - right
                counter[nums[left]] -= 1
                if counter[nums[left]] == 0:
                    del counter[nums[left]]
                left += 1
            right += 1
        return count 

        