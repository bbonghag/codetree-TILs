a,b = map(int, input().split())

n = 1

for i in range(1,b+1):
    if i % a == 0:
        n *= i

print(n)