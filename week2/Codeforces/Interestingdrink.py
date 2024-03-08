from bisect import bisect_right
n = int(input())
shops = list(map(int, input().split()))
shops.sort()
for _ in range(int(input())):
    q = int(input())
    pos = bisect_right(shops, q)
    print(pos)