b,a = map(int, input().split())


# b,a는 홀수라고 정의되어 있으므로 조건문을 줄 필요가 없음
for i in range(b,a-1, -2):
    # if i % 2 != 0:
    #     print(i, end=' ')
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