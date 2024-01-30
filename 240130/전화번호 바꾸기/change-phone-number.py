call = input()
n = call.split('-')[0]
x = call.split('-')[1]
y = call.split('-')[2]

# 내 풀이
# print(('-').join((n,y,x)))

# 해설
print(f"010-{y}-{x}")