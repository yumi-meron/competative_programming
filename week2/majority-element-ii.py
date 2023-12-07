class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # dic is dictionary to store the number of apperance of all elements
        dic = Counter(nums)
        n = len(nums) // 3 # n is the min apperance needed to consider an element as an answer
        ans = []

        for key in dic.keys():
            if dic[key] > n:
                ans.append(key)
                
        return ans

        