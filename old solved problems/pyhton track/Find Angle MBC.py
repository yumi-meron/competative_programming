from math import degrees, atan2
AB, BC = int(input()), int(input())
angle_btwn = round(degrees(atan2(AB, BC)))
print(str(angle_btwn), chr(176), sep='' )
