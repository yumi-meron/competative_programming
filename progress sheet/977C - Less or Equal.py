n , k = map(int, input().split())
nums = sorted(list(map(int, input().split())))
lst = [1]+nums
if k == n or lst[k+1] - lst[k] !=0:
    print(lst[k])
else:
    print(-1)
