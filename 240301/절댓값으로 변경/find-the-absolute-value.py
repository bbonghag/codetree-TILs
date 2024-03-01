n = int(input())
n_list = list(map(int, input().split()))

def abs_(n_list):
    for i in n_list:
        if i < 0:
            print(i*-1, end=' ')
        else:
            print(i, end=' ')
            
abs_(n_list)