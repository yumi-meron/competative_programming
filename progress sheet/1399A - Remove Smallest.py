t = int(input())
for i in range(t):
    n =int(input())
    nums = sorted(set(map(int, input().split())))
    if len(nums) == 1:
        print("YES")
    else:
        for j in range(len(nums)-1):
            if abs(nums[j] - nums[j+1]) > 1:
                print("NO")
                break
                
        else:
            print("YES")


