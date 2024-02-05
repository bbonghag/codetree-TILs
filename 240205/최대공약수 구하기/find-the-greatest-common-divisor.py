n,m = map(int, input().split())

def max_nxm(n,m):
    d = []
    if m % n == 0:
        print(n)
    elif n % m == 0:
        print(m)
    else:
        for i in range(1,101):
            if (m % i == 0) & (n % i == 0):
                d.append(i)
        print(max(d))

max_nxm(n,m)