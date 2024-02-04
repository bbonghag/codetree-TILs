# 내 풀이
n = int(input())

for i in range(n-1,-1,-1):
    for _ in range(i+1):
        print('*',end=" ")
    print()

# 해설 
# 변수 선언 및 입력
# n = int(input())

# # 길이가 n인 직각삼각형을 출력합니다.
# for i in range(n): # i = 0,1,2,3,4... n
# 	for _ in range(n-i): # n-0, n-1, n-2 ... 큰 수에서 1까지 작아져서 for문 도는 횟수가 점차 줄어듬
# 		print("*", end=" ")
# 	print()