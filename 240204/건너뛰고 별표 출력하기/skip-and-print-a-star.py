n = int(input())
cnt = 0

for i in range(1, n + n):
    print(i*'*','\n')
    cnt += 1
    if cnt == n:
        break

for j in range(n-1, 0, -1):
    print(j*'*','\n')