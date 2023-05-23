import math
import os
import random
import re
import sys

def insertionSort1(n, arr):
   
    last_elmnt = arr[-1]
    for i in range(n-2, -1, -1):
        if last_elmnt < arr[i]:
            arr[i+1] = arr[i]
            print(*arr)
        else:
            arr[i+1] = last_elmnt
            print(*arr)
            break
        if i==0:
            arr[i] = last_elmnt
            print(*arr)
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
