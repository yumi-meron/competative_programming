class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        num = max(heights)
        lst = [0 for i in range(num+1)]

        ans = []
        for i in range(len(names)):
            lst[heights[i]] = names[i]
       
        for j in range(num,-1,-1):
            if lst[j] != 0:
                ans.append(lst[j])
        return ans

            

        # for i in range(len(names)):
        #     for j in range(i+1,len(names)):
        #         if heights[i] < heights[j]:
        #             heights[i], heights[j] = heights[j], heights[i]
        #             names[i], names[j] = names[j], names[i]
        # return names
        