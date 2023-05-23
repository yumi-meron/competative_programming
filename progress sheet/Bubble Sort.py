#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    # Write your code here
    count = 0
    for i in a:
        for j in range(len(a)-1):
            if a[j] > a[j+1]:
                swap(a[j], a[j+1])
                count += 1
    print(f"Array is sorted in {count} swaps.\nFirst Element: {a[0]}\nLast Element: {a[-1]}")
    
           

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
