class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        dic = {}
        
        for i in range(len(arr2)):
            dic[arr2[i]] = i
        
        lst = list(set(arr1)-set(arr2))
        lst.sort()
        n = len(dic)

        for i in range(len(lst)):
            dic[lst[i]] = i + n

        arr1.sort(key = lambda i:dic[i])
        
        return arr1

            
                

        
        