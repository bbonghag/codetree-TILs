n = int(input())
n_list = list(map(int, input().split()))

def abs_(n_list):
    for i in n_list:
        if i < 0:
            print(i*-1, end=' ')
        else:
            print(i, end=' ')
            
abs_(n_list)


# 해설
# n을 n의 절대값으로 변경
# def absolute_value(arr):
#     for i in range(n):
#         if arr[i] < 0:
#             arr[i] = -arr[i]
    
#     return


# absolute_value(arr)


# for elem in arr:
#     print(elem, end=" ")