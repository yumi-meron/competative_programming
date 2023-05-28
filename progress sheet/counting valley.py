import math
import os
import random
import re
import sys

def countingValleys(steps, path):
    # Write your code here
    num_of_val = 0
    paths = []
    x = 0
    for i in path:
        if i == "U":
            x+=1
        elif i == "D":
            x-= 1
        paths.append(x)

    for j in range(len(path)):
        if paths[j] == 0 and paths[j-1]<0:
            num_of_val += 1
    return  num_of_val       
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
