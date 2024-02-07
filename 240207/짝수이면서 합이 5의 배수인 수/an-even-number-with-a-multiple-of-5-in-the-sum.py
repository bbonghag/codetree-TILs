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