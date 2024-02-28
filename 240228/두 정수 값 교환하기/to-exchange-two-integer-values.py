a,b = map(int, input().split())

def swap(a,b):
    a,b = b,a
    return a,b

n,m = swap(a,b)
print(n,m)