i = input()
o = input()

def check(i,o):
    for idx, n in enumerate(i):
        if o[0] == n:
            if o == i[idx:idx+len(o)]:
                return idx 
    else:
        return -1

result = check(i,o)
print(result)