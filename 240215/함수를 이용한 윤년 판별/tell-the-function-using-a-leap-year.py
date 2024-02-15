y = int(input())

def year(y):
    yeee = False
    if y % 4 == 0:
        yeee = True
    if (y % 100 == 0) & (y % 4 == 0):
        yeee = False
    if (y % 100 == 0) & (y % 4 == 0) & (y % 400 == 0):
        if y < 400:
            yeee = False
        else:
            yeee = True
    return yeee

result = year(y)

if result:
    print('true') 
else:
    print('false')