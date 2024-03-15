n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def check(a,b):
    nn = 0 
    for idx, n in enumerate(a):

        if n == b[0]:
            # print('yeeeeeeeeeeee')
            # print(a[idx:idx+len(b)])
            # print(b)
            if a[idx:idx+len(b)] == b:
                return 'Yes'
            
    else:
        return 'No'


result = check(a,b)
print(result)

# if check(a,b):
#     print('Yes')
# else:
#     print('No')