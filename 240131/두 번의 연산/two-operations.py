a = int(input())

# if a % 2 != 0:
#     a += 3
#     if a % 3 == 0:
#         print(int(a/3))
#     else:
#         print(a)

# else:
#     if a % 3 == 0:
#         print(int(a/3))
#     else:
#         print(a)

# 해설 - 아 조건에 맞을 경우에만 연산을 하면 되니까 굳이 else로 아닐 경우를 적어줄 필요가 없음
if a % 2 == 1:
    a += 3
    
if a % 3 == 0:
    a //= 3

print(a)