b,a = map(int, input().split())


for i in range(b,a-1, -1):
    if i % 2 != 0:
        print(i, end=' ')


# 생각난 예시
# for i in range(7,1,-1):
#   print(i)

# 7
# 6
# 5
# 4
# 3
# 2