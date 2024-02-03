a,b = map(int, input().split())

cnt = 0

for n in range(a,b+1):
    if (1920 % n == 0) & (2880 % n == 0):
        cnt += 1
    else:
        pass

if cnt:
    print(1)
else:
    print(0)