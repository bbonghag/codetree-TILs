y = int(input())

def year(y):
    if (y % 100 == 0) & (y % 4 == 0) & (y % 400 == 0):
        return True

    if (y % 100 == 0) & (y % 4 == 0):
        return False   

    if y % 4 == 0:
        return True



result = year(y)

if result:
    print('true') 
else:
    print('false')