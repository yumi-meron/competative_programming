if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    if query_name in student_marks.keys():
        values = list(student_marks[query_name])
        sum = 0
        for i in values:
            sum += i
        average = sum/len(values)
        print('%.2f' %average)
        
