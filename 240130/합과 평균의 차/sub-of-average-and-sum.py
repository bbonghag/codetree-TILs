a,b,c = map(int, input().split())

sum = a+b+c
mean = int(sum/3)
m = int(sum - mean) 

print(sum, '\n', mean, '\n', m, sep='')