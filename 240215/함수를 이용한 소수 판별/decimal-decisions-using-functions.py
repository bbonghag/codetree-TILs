a,b = map(int, input().split())

def prime(a,b):

    p = []

    
    for n in range(a,b+1):
        is_prime = True

        for i in range(2, n):
            if n % i == 0:
                is_prime = False

        if is_prime:
            p.append(n)

    return sum(p)

result = prime(a,b)
print(result)