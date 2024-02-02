n = int(input())

count = 0
a = 1

while True:
    d = n //a
    count += 1
    a +=1
    
    if d <= 1:
        break
    else:
        n = d

print(count)

# 해설 - for문도 가능
# for i in range(1, 101):
#     if n <= 1:
#         print(cnt)
#         break
#     n //= i
#     cnt += 1


# 해설 - 아 while에 조건을 걸면 좀 더 코드가 간단해지겠구나! 
# i = 1
# while n > 1:
#    n //= i
#    i += 1
#    cnt += 1

# print(cnt)