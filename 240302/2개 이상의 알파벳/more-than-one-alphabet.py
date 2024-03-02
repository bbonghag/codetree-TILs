a = input()

def abc(a):
    a = list(a)

    for i in a:
        # print(a.count(i))
        if a.count(i) > 1:
            return True
    else:
        return False



# abc(a)
result = abc(a)
if result:
    print('Yes')
else:
    print('No')