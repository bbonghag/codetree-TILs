a,b = map(int, input().split())

def abc(a,b):
    if a > b:
        a *= 2
        b += 10
    else:
        a += 10
        b *= 2
    return a,b

n1, n2 = abc(a,b)
print(n1, n2)