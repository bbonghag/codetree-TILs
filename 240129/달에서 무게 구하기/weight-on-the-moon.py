a,b = 13, 0.165
b = float(f'{b:.6f}') # 소수점 자리를 맞춰주면 str로 타입이 바뀜

c = "%.6f" % (a*b)


print(f'{a} * {b} = {c}')

# 소수점 표현하는 방법 3가지
# print("%.4f" % a)
# print("{0:.4f}".format(a))
# print(f"{a:.4f}")