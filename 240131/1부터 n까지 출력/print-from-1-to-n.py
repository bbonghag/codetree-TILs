# 내 답안
n = int(input())

list_ = []

for i in range(1,n+1):
    list_.append(str(i))

# print((' ').join(list_))


# 해설 답안
for i in range(1,n+1):
    print(i, end=' ')