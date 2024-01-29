a,b = 13, 0.165




print(f'{a} * {b:.6f} = {a*b:.6f}')
# print(a,'*', ("%.6f" % b),'=', ("%.6f" %  (a*float(("%.6f" % b)))) )
# 포맷팅 사용하는게 가장 깔끔한 것 같음. 

# 소수점 표현하는 방법 3가지
# print("%.4f" % a)
# print("{0:.4f}".format(a))
# print(f"{a:.4f}")