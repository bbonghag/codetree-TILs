age_sum = 0
count = 0

while True:
    age = int(input())
    if 19 < age < 30:
        age_sum += age
        count += 1
    else:
        result = round((age_sum/count), 2)
        print(f"{result:.2f}")    
        break # 특정 조건에서 while문을 끊어주지 않으면 EOFError뜸. 


# 해설 - 꼭 else까지 쓸 필요없이 if 하나만으로도 충분함
# # 변수 선언
# sum_val = 0
# cnt = 0

# # 언제 끝날지 모르므로
# # 계속 반복합니다.
# while True:
#     # 변수를 선언하고 입력을 받습니다.
#     n = int(input())

#     # 입력받은 값이 20대가 아니면 종료합니다.
#     if n >= 30 or n <= 19:
#         print(f"{sum_val/cnt:.2f}")
#         break
    
#     # 20대가 맞는 경우에는, 계속 값을 계산해줍니다.
#     sum_val += n
#     cnt += 1