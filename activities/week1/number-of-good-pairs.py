from collections import Counter
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dic = Counter(nums)
        summ = 0
        for i in dic.keys():
            if dic[i]>1:
                summ += dic[i]*(dic[i]-1)//2
        return summ
        
        