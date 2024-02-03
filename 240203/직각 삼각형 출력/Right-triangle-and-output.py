n = int(input())
k = 1

for _ in range(1,n+1):
    print(k*'*')
    k += 2

# 해설 - n번만큼 1차 for문을 돌리고 2차 for문에서 각 순서마다 2씩 증가가시킨 개수만큼 *을 출력하도록 함
# 그래도 for문을 2개 돌리는 것 보다 하나만 돌리리는게 시간이나 연산면으로 조오오금 더 낫지 않을까
# 변수 선언 및 입력
# n = int(input())

# # 길이가 n인 직각삼각형을 출력합니다.
# for i in range(n):
# 	for _ in range(2 * i + 1):
# 		print("*", end="")
# 	print()