n = int(input())

def yesorno(n):
    n_10 = n // 10
    n_1 = n % 10
    if n % 2 == 0 and (n_10 + n_1) % 5 == 0:
        return 'Yes'
    else:
        return 'No'

result = yesorno(n)
print(result)

# 해설 - 하나의 함수 안에 다 넣어도 되지만 출력값의 형태에 따라 bool타입을 통해
# 결과를 출력하는 것도 방법 중 하나
# 변수 선언 및 입력:
# n = int(input())


# def is_magic_number(n):
#     return n % 2 == 0 and (n // 10 + (n % 10)) % 5 == 0


# if is_magic_number(n):
#     print("Yes")
# else:
#     print("No")