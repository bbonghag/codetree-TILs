a = input()

def pal(a):
    n = list(a)
    reversed_n = n[::-1]
    new_n = ''.join(reversed_n)
    if n == reversed_n:
        print('Yes')
    else:
        print('No')

pal(a)