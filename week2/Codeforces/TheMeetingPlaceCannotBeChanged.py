n = int(input())
positions = list(map(int, input().split()))
speed = list(map(int, input().split()))
mid = sum(positions) / n
def check(sec):
    global mid
    left = float('inf')
    right = float('-inf')
    for i,pos in enumerate(positions):
        if pos <= mid:
            loc = (speed[i] * sec) + pos
            left = min(left,loc)
        else:
            loc = pos - (speed[i] * sec)
            right = max(right, loc)
    if right <= left:
        return True
    return False
 
 
minn = 0
maxx = max(positions) - min(positions)
ans = maxx
while maxx - minn > 1e-7:
    middle = (minn + maxx) / 2
    if check(middle):
        ans = middle
        maxx = middle
    else:
        minn = middle
print(ans)