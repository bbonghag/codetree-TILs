a,b = map(int, input().split())

def modify(a,b):
    # n1 = max(a,b) + 25
    # n2 = min(a,b) * 2
    # print(n2, n1)
    if a > b:
        a += 25
        b *= 2
    else:
        b += 25
        a *=2 
    # print(a,b)
    return a,b



n1, n2 = modify(a,b)
print(n1, n2)