a = int(input())
b,c,d,e = map(int, input().split())

for n in [b,c,d,e]:
    if a > n:
        print(1)
    else:
        print(0)