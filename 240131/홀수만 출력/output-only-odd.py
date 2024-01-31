# 내 답안 - a,b 는 홀수라고 조건을 줬으므로 굳이 조건문을 쓸 필요가 없었음
# a,b = map(int, input().split())

# for i in range(a,b+1):
#     # print(i, end=' ')
#     if i % 2 != 0:
#         print(i, end=' ')


# 해설
for i in range(a,b+1,2):
    print(i, end=' ')