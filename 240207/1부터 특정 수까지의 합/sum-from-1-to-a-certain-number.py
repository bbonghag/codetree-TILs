n = int(input())

def cal(n):
    s = 0
    for i in range(1,n+1):
        s += i
    # print(s)
    return s//10


result = cal(n)
print(result)