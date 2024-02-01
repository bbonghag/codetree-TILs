a,b = map(int, input().split())

if a > 0 and type(a) is not float:
    for _ in range(b):
        print(a, end='')
else:
    print(0)