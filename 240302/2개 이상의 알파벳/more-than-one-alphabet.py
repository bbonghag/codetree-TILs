a = input()

def abc(a):
    a = list(a)
    cnt = 0
    for i in a:
        # print(a.count(i))
        if a.count(i) != 1:
            cnt += a.count(i)
        else:
            cnt += a.count(i)

    # print(cnt)
    # print(len(a))
    if cnt != len(a):
        return 'Yes'
    else:
        return 'No'

# abc(a)
result = abc(a)
print(result)