count = 0
age_sum = 0

while True:
    num = int(input())
    if num < 30:
        age_sum += num
        count += 1
    else:
        break

n = round((age_sum/count), 3)

print(f"{n:.2f}")