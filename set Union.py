if __name__ == '__main__':
    n = int(input())
    english = set(map(int, input().split()))
    b = int(input())
    french = set(map(int, input().split()))  
    union = english.union(french) 
    print(len(union))
    
