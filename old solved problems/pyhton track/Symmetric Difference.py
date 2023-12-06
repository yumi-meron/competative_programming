# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    M = int(input())
    set1 = set(map(int, input().split()))
    N = int(input())
    set2 = set(map(int, input().split()))
    union = set1.union(set2)
    inter = set1.intersection(set2)
    difference = sorted(union.difference(inter))
    for i in difference:
        print(i)
        
        
