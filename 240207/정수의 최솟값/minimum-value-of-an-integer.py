a,b,c = map(int, input().split())

def n_min(a,b,c):
    # return min([a,b,c])
    tem_m = a
    if a > b:
        tem_m = b
    if tem_m > c:
        tem_m = c
    
    return tem_m

m = n_min(a,b,c)
print(m)