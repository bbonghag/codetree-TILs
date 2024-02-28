n = int(input())
n_list = list(map(int, input().split()))

def pre(n_list):
    for i, n in enumerate(n_list):
        if n % 2 == 0:
            n_list[i] = int(n / 2)

pre(n_list)

for i in n_list:
    print(i, end=' ')