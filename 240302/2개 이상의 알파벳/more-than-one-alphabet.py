a = input()

def abc(a):

    lang = len(a)
    for i in range(lang):
        if a[i] != a[0]:
            return True

    return False


# abc(a)
result = abc(a)
if result:
    print('Yes')
else:
    print('No')