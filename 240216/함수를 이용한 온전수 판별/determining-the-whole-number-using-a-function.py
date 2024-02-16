a,b = map(int, input().split())


def process(n):
    if n % 2 == 0:
        return False
    elif n % 10 == 5:
        return False
    elif (n % 3 == 0) & (n % 9 != 0):
        return False
    else:
        return True

cnt = 0
for n in range(a, b+1):
    if process(n):
        cnt += 1


print(cnt)