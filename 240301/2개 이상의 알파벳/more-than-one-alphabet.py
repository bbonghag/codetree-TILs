a = input()

def abc(a):
    a = list(a)
    for i in a:
        # print(a.count(i))
        if a.count(i) != 1:
            return 'No'
        else:
            return 'Yes'

# abc(a)
result = abc(a)
print(result)