a,b = map(int, input().split())

def process(n):
    
    is_prime = True

    if n == 1:
        is_prime = False 

    for i in range(2,n):
        if n % i == 0:
            is_prime = False

            
    if is_prime == True:
            n_10 = n // 10
            n_1 = n % 10
            # print('n_1 : ', n_1)
            # print('n_10 : ', n_10)
            if (n_1 + n_10) % 2 == 0:
                return True
    return False 
cnt = 0
for n in range(a,b+1):
    if process(n):
        cnt += 1 

print(cnt)