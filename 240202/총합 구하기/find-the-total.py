a,b = map(int, input().split())

n_sum = 0

for n in range(a, b+1):
    if n % 6 == 0 and n % 8 != 0:
        n_sum += n

print(n_sum)