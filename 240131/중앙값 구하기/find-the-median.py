# 내 답안
# n = list(map(int, input().split()))

# max_n = max(n)
# min_n = min(n)

# n.remove(max_n)
# n.remove(min_n)
# print(n[0])



# 해설 - 3개의 숫자에서 나올 수 있는 경우의 수를 고려하여 조건문으로 만듬
a,b,c = map(int, input().split())

# 출력
if a > b:
    if c > a:
        # a > b, c > a 일때 (c > a > b)
        print(a)
    # a > b, a > c 일때 (a가 가장 크고, b와 c중 더 큰 수가 중앙값)
    elif b > c:
        print(b)
    else:
        print(c)
else:
    if c > b:
        # b > a, c > b 일때 (c > b > a)
        print(b)
    # b > a, b > c 일때 (b가 가장 크고, a와 c중 더 큰 수가 중앙값)
    elif a > c:
        print(a)
    else:
        print(c)