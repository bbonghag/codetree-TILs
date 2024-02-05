# 내 풀이 - 
n,m = map(int, input().split())

def max_nxm(n,m):
    d = []
    if m % n == 0:
        print(n)
    elif n % m == 0:
        print(m)
    else:
        for i in range(1,101):
            if (m % i == 0) & (n % i == 0):
                d.append(i)
        print(max(d))

max_nxm(n,m)

# 해설  
# 이걸보니 최대 공약수가 될 수 있는건 둘 중 작은 수이므로 굳이 100까지 for문을 돌릴 필요가 없음. 
# 둘 중 작은 수를 기준으로 for문을 돌려도됨
# 그리고 for문을 돌수록 더 큰 값이 나오면서 결국에는 가장 큰값으로 m,n 둘중 하나의 값이 나오기때문에
# 따로 리스트에 추가해서 최대값을 구할 필요가 없음

# n과 m의 최대공약수를 반환합니다.
# def find_gcd(n, m):
#     gcd = 0
#     for i in range(1, min(n, m) + 1):
#         if n % i == 0 and m % i == 0:
#             gcd = i

#     print(gcd)


# find_gcd(n, m)