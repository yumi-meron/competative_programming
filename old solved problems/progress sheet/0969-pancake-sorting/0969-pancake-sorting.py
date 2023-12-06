class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]: 
        ar = sorted(arr)
        ans = []
        i = 0
        j = len(arr)-1
        while(arr != ar and i<j):
            max_val= max(list(arr[i:j+1]))
            ind = arr.index(max_val)
            arr[i:ind+1] = list(reversed(arr[i:ind+1]))
            arr[:j+1] = list(reversed(arr[:j+1]))
            ans.append(ind+1)
            ans.append(j+1)
            j-=1
        
        return ans 
            
            
        