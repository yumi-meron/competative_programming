class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        greatest = counter.most_common(1)[0][0]
        return greatest
        