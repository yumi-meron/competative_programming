class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        state = 'inc'
        change = 0
        maxx = max(arr)
        if len(arr) < 3 or (maxx == arr[0] or maxx == arr[-1]):
            return False
        for i in range(1,len(arr)):
            if arr[i-1] == arr[i] :
                return False
            elif state == 'inc'and (arr[i-1] > arr[i]):
                state = 'dec'
                change += 1
            elif state == 'dec'and arr[i-1] < arr[i]:
                change += 1
            if change > 1:
                return False
        return change > 0

                
        