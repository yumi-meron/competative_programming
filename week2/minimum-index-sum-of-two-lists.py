class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dic1 = {res: i for i,res in enumerate(list1)}
        dic2 = {res: i for i,res in enumerate(list2)}

        common = set(list1) & set(list2)
        min_sum = float('inf')
        ans = []

        for res in common:
            idx_sum = dic1[res] + dic2[res]
            if idx_sum < min_sum:
                min_sum = idx_sum
                ans = [res]
            elif idx_sum == min_sum:
                ans.append(res)
        return ans



            