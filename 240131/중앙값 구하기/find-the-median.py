n = list(map(int, input().split()))

max_n = max(n)
min_n = min(n)

n.remove(max_n)
n.remove(min_n)
print(n[0])