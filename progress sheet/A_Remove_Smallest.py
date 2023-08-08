t = int(input())
for i in range(t):
    n =int(input())
    nums = sorted(set(map(int, input().split())))
    if len(nums)==1:
        print("YES")
    else:
        arr = [j for j in range(nums[0],nums[-1]+1)]
        if nums == arr:
            print("YES")
        else:
            print("NO")
