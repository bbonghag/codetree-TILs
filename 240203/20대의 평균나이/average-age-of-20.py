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