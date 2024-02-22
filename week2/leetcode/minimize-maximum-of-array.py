class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        # maxx = nums[0]
        # i, j = 0, 1

        # while j < len(nums):
        #     if nums[j] > maxx:
        #         x = nums[j] - nums[i]
        #         # print(i,j)
        #         # print(nums[i], nums[j])
        #         rem = (x) % 2
        #         # print(rem)
        #         # print(x//2)
        #         nums[j] -= (x // 2) + rem
        #         nums[i] += ((x) // 2) + rem
        #         # print(nums)
        #         maxx = max(maxx,nums[i])
        #     else:
        #         if nums[i] < nums[j] and nums[i] + ((nums[j] - nums[i])//2) <= maxx:
        #             nums[i], nums[j] = nums[j], nums[i]
        #         else:
        #             x = maxx - nums[i]
        #             if nums[j] - x > 0:
        #                 nums[j] -= x
        #                 nums[i] += x
        #         # print(nums)
        #     i+=1
        #     j+=1
        # return maxx
        maxx = nums[0]
        runsum = nums[0]
        for i in range(1,len(nums)):
            runsum += nums[i]
            if nums[i] > maxx:
                ave = math.ceil((runsum) / (i+1))
                maxx = max(maxx, ave)
        return maxx





