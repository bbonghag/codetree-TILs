cnt = 0
for _ in range(5):
    n = int(input())
    if n % 3 == 0:
        cnt += 1
    
if cnt == 5:
    print(1)
else:
    print(0)

# 해설 - bool타입을 주로 이용함.더하는 과정을 생략할 수 있어서 이것도 괜찮아보임
# # 변수 선언 및 입력
# satisfied = True
	
# for _ in range(5):
#     # 모든 수가 3의 배수인지 확인합니다.
#     a = int(input())
#     if a % 3 != 0:
#         satisfied = False

# #출력
# if satisfied == True:
#     print("1")
# else:
#     print("0")