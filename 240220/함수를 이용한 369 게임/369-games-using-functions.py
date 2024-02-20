a,b = map(int, input().split())

def preprocess(n):
    while n > 0:
        if (n%10) in [3,6,9]:
            return True
        n //= 10
    return False

def preprocess2(n):
    if preprocess(n) or (n % 3 == 0):
        return True



cnt = 0
for n in range(a,b+1):
    if preprocess2(n):
        cnt += 1 



print(cnt)