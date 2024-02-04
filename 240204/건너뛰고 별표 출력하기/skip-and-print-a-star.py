n = int(input())

# 첫번째 내 풀이
# cnt = 0

# for i in range(1, n + n):
#     print(i*'*','\n')
#     cnt += 1
#     if cnt == n:
#         break

# for j in range(n-1, 0, -1):
#     print(j*'*','\n')


####################################
# 두번째 내 풀이

cnt = 1

for _ in range(n):
    print(cnt*'*','\n')
    cnt += 1
    if cnt == n+1:
        for i in range(n-1,0,-1):
            print(i*'*','\n')
            # print(i)