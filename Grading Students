import math
import os
import random
import re
import sys

def gradingStudents(grades):
    
    for i in range(0, len(grades)):
        if grades[i]<38:
            continue
        else:
            x = grades[i]
            y = x%5
            if y == 3:
                grades[i] += 2
            elif y == 4:
                grades[i] += 1
            else:
                continue
    return grades
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
