n = int(input())

count = 0
a = 1

while True:
    d = n //a
    count += 1
    a +=1
    
    if 1 >= d:
        break
    else:
        n = d

print(count)