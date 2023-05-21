if __name__ == '__main__':
    N = int(input())
    my_set = set()
    for i in range(N):
        c_stamps = input()
        my_set.add(c_stamps)
    print(len(my_set))
        
