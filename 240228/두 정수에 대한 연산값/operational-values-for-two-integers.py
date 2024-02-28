a,b = map(int, input().split())

def modify(a,b):
    n1 = max(a,b) + 25
    n2 = min(a,b) * 2
    print(n2, n1)

modify(a,b)