import math
m, n, a = map(int, input().split())
area = math.ceil(m/a) * math.ceil(n/a)
print(area)
