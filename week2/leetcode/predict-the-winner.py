class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def func(left, right):
            if left > right:
                return 0
            left_choice = nums[left] - func(left + 1, right)
            right_choice = nums[right] - func(left, right - 1)

            return  max(left_choice, right_choice)
        ans = func(0,len(nums)-1)
        if ans >= 0:
            return True
        return False