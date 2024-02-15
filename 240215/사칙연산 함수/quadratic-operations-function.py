a,o,c = input().split()
a,c = map(int, [a,c])


def process(a,o,c):
    if o == '+':
        return f'{a} + {c} = {a+c}'   
    if o == '-':
        return f'{a} - {c} = {a-c}'  
    if o == '/':
        return f'{a} / {c} = {a/c}'
    if o == '*':
        return f'{a} * {c} = {a*c}'

result = process(a,o,c)
print(result)